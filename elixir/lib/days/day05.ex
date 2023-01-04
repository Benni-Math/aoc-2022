defmodule Days.Day05 do
  @moduledoc """
  Solutions to AoC 2022 Day 5: Supply Stacks.
  """

  # Public Functions
  @spec pt1(binary()) :: binary()
  @spec pt2(binary()) :: binary()

  # Types
  @typep crates :: list(list(char())) # might want to change this to a tuple(list(char))
  @typep move :: %{move: integer(), from: integer(), to: integer()}

  # Private Functions
  @spec init(binary()) :: list(list(binary))
  @spec parse_move(binary()) :: move()
  @spec parse_crates(list(binary())) :: crates()
  @spec add_row(binary(), crates()) :: crates()
  @spec exec_move_9000(move(), crates()) :: crates()
  @spec exec_move_9001(move(), crates()) :: crates()

  @doc """
  Part 1: CrateMover 9000.

  ## Examples

    iex> Days.Day05.pt1(day05_input) # filename
    <Solution to Day 5, part 1>

  """
  def pt1(file_name) do
    [init_state, move_set] = init(file_name)

    move_set
      |> Enum.map(&parse_move/1)
      |> Enum.reduce(parse_crates(init_state), &exec_move_9000/2)
      |> Enum.map(&hd/1)
      |> List.to_string()
  end

  @doc """
  Part 2: CrateMover 9001.

  ## Examples

    iex> Days.Day05.pt2(day05_input) # filename
    <Solution to Day 5, part 2>

  """
  def pt2(file_name) do
    [init_state, move_set] = init(file_name)

  move_set
    |> Enum.map(&parse_move/1)
    |> Enum.reduce(parse_crates(init_state), &exec_move_9001/2)
    |> Enum.map(&hd/1)
    |> List.to_string()
  end

  # --------------- Private Functions --------------- #

  defp init(file_name) do
    File.stream!(file_name)
      |> Stream.map(&(String.trim(&1, "\n")))
      |> Enum.chunk_by(&(&1 == ""))
      |> List.delete_at(1)
  end

  defp parse_move(move_str) do
    str_list = move_str |> String.split(" ")
    str_list
      |> Enum.take_every(2)
      |> (fn list ->
          [
            Enum.map(list, &String.to_atom/1),
            Enum.map(str_list -- list, &String.to_integer/1),
          ]
        end).()
      |> Enum.zip()
      |> Map.new()
  end

  defp parse_crates(init_state) do
    succ = &(&1 + 1)
    num_stacks = init_state
      |> hd()
      |> String.length()
      |> div(4)
      |> succ.()

    crate_stacks = 1..num_stacks
      |> Enum.to_list()
      |> Enum.map(fn _ -> [32] end)

    init_state
      |> Enum.reverse()
      |> tl()
      |> Enum.reduce(crate_stacks, &add_row/2)
  end

  defp add_row(row, crate_stacks) do
    is_alphabetic = fn c -> (c > 64 && c < 91) || (c > 96 && c < 123) end
    row
      |> String.to_charlist()
      |> Enum.chunk_every(4)
      |> Enum.map(&(Enum.find(&1, is_alphabetic)))
      |> Enum.with_index()
      |> Enum.map(fn {c, index} ->
        if c do
          [c | Enum.at(crate_stacks, index)]
        else
          Enum.at(crate_stacks, index)
        end
      end)
  end

  defp exec_move_9000(move, crate_stacks) do
    %{
      move: num_to_move,
      from: from,
      to: to,
    } = move

    crate_mover = fn {from, to}, curr_stack ->
      [crate_to_move | from_stack] = Enum.at(curr_stack, from)
      to_stack = [crate_to_move | Enum.at(curr_stack, to)]

      curr_stack
        |> List.replace_at(from, from_stack)
        |> List.replace_at(to, to_stack)
    end

    1..num_to_move
      |> Enum.map(fn _ -> {from - 1, to - 1} end)
      |> Enum.reduce(crate_stacks, crate_mover)
  end

  defp exec_move_9001(move, crate_stacks) do
    # TODO:
    %{
      move: num_to_move,
      from: from,
      to: to,
    } = move

    {crates_to_move, from_stack} = crate_stacks
      |> Enum.at(from-1)
      |> Enum.split(num_to_move)

    to_stack =  crates_to_move ++ Enum.at(crate_stacks, to-1)

    crate_stacks
      |> List.replace_at(from-1, from_stack)
      |> List.replace_at(to-1, to_stack)
  end
end
