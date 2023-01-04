defmodule Days.Day01 do
  @moduledoc """
  Solutions to AoC 2022 Day 1: Calorie Counting.
  """

  # Public Functions
  @spec pt1(binary()) :: integer()
  @spec pt2(binary()) :: integer()

  # Types
  @typep max_acc :: %{max: integer(), sum: integer()}
  @typep triple_int :: {integer(), integer(), integer()}
  @typep max_3_acc :: %{max: triple_int(), sum: integer()}

  # Private Functions
  @spec track_max(binary(), max_acc()) :: max_acc()
  @spec track_top_three(binary(), max_3_acc()) :: max_3_acc()
  @spec index_of_min(tuple()) :: integer()

  @doc """
  Part 1: find the elf with the max calories.

  ## Examples

    iex> Days.Day01.pt1(day01_input) # filename
    <Solution to Day 1, part 1>

  """
  def pt1(file_name) do
    File.stream!(file_name)
      |> Stream.map(&String.trim/1)
      |> Enum.reduce(%{max: 0, sum: 0}, &track_max/2)
      |> Map.get(:max)
  end

  @doc """
  Part 2: find top three calorie-carrying elves.

  ## Examples

    iex> Days.Day01.pt2(day01_input) # filename
    <Solution to Day 1, part 2>

  """
  def pt2(file_name) do
    File.stream!(file_name)
      |> Stream.map(&String.trim/1)
      |> Enum.reduce(%{max: {0, 0, 0}, sum: 0}, &track_top_three/2)
      |> Map.get(:max)
      |> Tuple.sum()
  end

  # --------------- Private Functions --------------- #

  defp track_max(x, acc) do
    cond do
      x == "" and acc.sum > acc.max ->
        %{
          max: acc.sum,
          sum: 0
        }
      x == "" ->
        %{
          max: acc.max,
          sum: 0
        }
      true ->
        val = String.to_integer(x)
        %{
          max: acc.max,
          sum: acc.sum + val,
        }
    end
  end

  defp track_top_three(x, acc) do
    min_index = index_of_min(acc.max)
    min_elem = elem(acc.max, min_index)
    cond do
      x == "" and acc.sum > min_elem ->
        %{
          max: put_elem(acc.max, min_index, acc.sum),
          sum: 0
        }
      x == "" ->
        %{
          max: acc.max,
          sum: 0
        }
      true ->
        val = String.to_integer(x)
        %{
          max: acc.max,
          sum: acc.sum + val,
        }
    end
  end

  defp index_of_min(tpl) do
    list = Tuple.to_list(tpl)
    Enum.with_index(list)
      |> List.foldl(0, fn {x, index}, min_index ->
          if x < elem(tpl, min_index) do
            index
          else
            min_index
          end
        end)
  end

end
