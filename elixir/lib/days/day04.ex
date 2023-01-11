defmodule Days.Day04 do
  @moduledoc """
  Solutions to AoC 2022 Day 4: Camp Cleanup.
  """

  # Public Functions
  @spec pt1(binary()) :: integer()
  @spec pt2(binary()) :: integer()

  # Types
  @typep range_map() ::  %{low: integer(), high: integer()}

  # Private Functions
  @spec parse_line(binary()) :: {range_map(), range_map()}
  @spec parse_range(binary()) :: range_map()
  @spec range_containment?({range_map(), range_map()}) :: boolean()
  @spec range_overlap?({range_map(), range_map()}) :: boolean()

  @doc """
  Part 1: How many elves' cleanup areas are contained in each other?

  ## Examples

    iex> Days.Day04.pt1(day04_input) # filename
    <Solution to Day 4, part 1>

  """
  def pt1(file_name) do
    reducer = fn x, acc ->
      case range_containment?(x) do
        true -> acc + 1
        false -> acc
      end
    end
    File.stream!(file_name)
      |> Stream.map(&String.trim/1)
      |> Stream.map(&parse_line/1)
      |> Enum.reduce(0, reducer)
  end

  @doc """
  Part 2: How many elves' cleanup areas overlap?

  ## Examples

    iex> Days.Day04.pt2(day04_input) # filename
    <Solution to Day 4, part 2>

  """
  def pt2(file_name) do
    reducer = fn x, acc ->
      case range_overlap?(x) do
        true -> acc + 1
        false -> acc
      end
    end
    File.stream!(file_name)
      |> Stream.map(&String.trim/1)
      |> Stream.map(&parse_line/1)
      |> Enum.reduce(0, reducer)
  end

  # --------------- Private Functions --------------- #

  defp parse_line(line) do
    String.split(line, ",")
      |> Enum.map(&parse_range/1)
      |> List.to_tuple()
  end

  defp parse_range(range) do
    [low, high] = String.split(range, "-") |> Enum.map(&String.to_integer/1)
    %{
      low: low,
      high: high,
    }
  end

  defp range_containment?({r1, r2}) do
    (r1.low <= r2.low && r2.high <= r1.high)
    || (r2.low <= r1.low && r1.high <= r2.high)
  end


  defp range_overlap?({r1, r2}) do
    (r1.low <= r2.low && r2.low <= r1.high)
    || (r2.low <= r1.low && r1.low <= r2.high)
  end
end
