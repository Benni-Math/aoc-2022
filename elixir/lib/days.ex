defmodule Days do
  @moduledoc """
  Documentation for `AOC`.
  """

  alias Days.{Day01, Day02, Day03, Day04, Day05, Day06, Day07}

  # Could I generate this list with a macro?
  @soln_functions [
    {&Day01.pt1/1, &Day01.pt2/1},
    {&Day02.pt1/1, &Day02.pt2/1},
    {&Day03.pt1/1, &Day03.pt2/1},
    {&Day04.pt1/1, &Day04.pt2/1},
    {&Day05.pt1/1, &Day05.pt2/1},
    {&Day06.pt1/1, &Day06.pt2/1},
    {&Day07.pt1/1, &Day07.pt2/1},
  ]

  @input_dir "../inputs/"

  defp inputs do
    Enum.map(1..25, fn i ->
      x = Integer.to_string(i)
      if String.length(x) == 1 do
        @input_dir <> "0" <> x <> ".txt"
      else
        @input_dir <> x <> ".txt"
      end
    end)
  end

  @doc """
  Runs all Advent of Code solutions.

  ## Examples

    iex> Days.run_all()

  """
  def run_all do
    for {day_name, file_name, {pt1, pt2}} <- Enum.zip([1..25, inputs(), @soln_functions]) do
      IO.puts "\nDay #{day_name}:"
      IO.puts "  Part 1: #{pt1.(file_name)}"
      IO.puts "  Part 2: #{pt2.(file_name)}"
    end
  end
end
