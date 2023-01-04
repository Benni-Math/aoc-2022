defmodule Days.Day06 do
  @moduledoc """
  Solutions to AoC 2022 Day 6: Tuning Trouble.
  """

  # Public Functions
  @spec pt1(binary()) :: integer()
  @spec pt2(binary()) :: integer()

  # Private Functions
  @spec find_marker(list(), integer()) :: integer()

  @doc """
  Part 1: Find start-of-packet marker.

  ## Examples

    iex> Days.Day06.pt1(day06_input) # filename
    <Solution to Day 6, part 1>

  """
  def pt1(file_name) do
    File.read!(file_name)
      |> String.to_charlist()
      |> find_marker(4)
  end

  @doc """
  Part 2: Find start-of-messaged marker.

  ## Examples

    iex> Days.Day06.pt2(day06_input) # filename
    <Solution to Day 6, part 2>

  """
  def pt2(file_name) do
    File.read!(file_name)
      |> String.to_charlist()
      |> find_marker(14)
  end

  # --------------- Private Functions --------------- #

  defp find_marker(list, marker_size) do
    list
      |> Enum.chunk_every(marker_size, 1, :discard)
      |> Enum.with_index()
      |> Enum.find(fn {clist, _i} -> Enum.uniq(clist) == clist end)
      |> elem(1)
      |> (&(&1 + marker_size)).()
  end
end
