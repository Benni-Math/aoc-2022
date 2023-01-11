defmodule Days do
  @moduledoc """
  Documentation for `AOC`.
  """

  @input_dir "../inputs/"

  alias Days.{
    Day01, Day02, Day03, Day04, Day05,
    Day06, Day07, Day08, Day09, Day10,
    Day11, Day12, Day13, Day14, Day15,
    Day16, Day17, Day18, Day19, Day20,
    Day21, Day22, Day23, Day24, Day25,
  }

  # Could I generate this list with a macro?
  @soln_functions [
    {&Day01.pt1/1, &Day01.pt2/1},
    {&Day02.pt1/1, &Day02.pt2/1},
    {&Day03.pt1/1, &Day03.pt2/1},
    {&Day04.pt1/1, &Day04.pt2/1},
    {&Day05.pt1/1, &Day05.pt2/1},
    {&Day06.pt1/1, &Day06.pt2/1},
    {&Day07.pt1/1, &Day07.pt2/1},
    {&Day08.pt1/1, &Day08.pt2/1},
    {&Day09.pt1/1, &Day09.pt2/1},
    {&Day10.pt1/1, &Day10.pt2/1},
    {&Day11.pt1/1, &Day11.pt2/1},
    {&Day12.pt1/1, &Day12.pt2/1},
    {&Day13.pt1/1, &Day13.pt2/1},
    {&Day14.pt1/1, &Day14.pt2/1},
    {&Day15.pt1/1, &Day15.pt2/1},
    {&Day16.pt1/1, &Day16.pt2/1},
    {&Day17.pt1/1, &Day17.pt2/1},
    {&Day18.pt1/1, &Day18.pt2/1},
    {&Day19.pt1/1, &Day19.pt2/1},
    {&Day20.pt1/1, &Day20.pt2/1},
    {&Day21.pt1/1, &Day21.pt2/1},
    {&Day22.pt1/1, &Day22.pt2/1},
    {&Day23.pt1/1, &Day23.pt2/1},
    {&Day24.pt1/1, &Day24.pt2/1},
    {&Day25.pt1/1, &Day25.pt2/1},
  ]

  defp inputs do
    input_dir = File.ls!(@input_dir)
    1..25
      |> Enum.map(&num_to_input_name/1)
      |> Enum.filter(fn input_name -> Enum.member?(input_dir, input_name) end)
      |> Enum.map(fn name -> @input_dir <> name end)
  end

  defp num_to_input_name(i) do
    x = Integer.to_string(i)
    if String.length(x) == 1 do
      "0" <> x <> ".txt"
    else
      x <> ".txt"
    end
  end

  @doc """
  Runs all Advent of Code solutions.

  ## Examples

    iex> Days.main()

  """
  def main(_args \\ []) do
    get_day_output = fn {day_name, file_name, {pt1, pt2}} ->
      "Day #{day_name}:\n  Part 1: #{pt1.(file_name)}\n  Part 2: #{pt2.(file_name)}\n"
    end

    [1..25, inputs(), @soln_functions]
      |> Enum.zip()
      |> Enum.map(&(Task.async(fn -> get_day_output.(&1) end)))
      |> Enum.map(&Task.await/1)
      |> Enum.each(&IO.puts/1)
  end
end
