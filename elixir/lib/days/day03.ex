defmodule Days.Day03 do
  @moduledoc """
  Solutions to AoC 2022 Day 3: Rucksack Reorganization.
  """

  # Public Functions
  @spec pt1(binary()) :: integer()
  @spec pt2(binary()) :: integer()

  # Private Functions
  @spec prio(integer()) :: integer()
  @spec shared_item(binary()) :: integer()
  @spec split_list(list()) :: {list(), list()}
  @spec list_overlap(list(), list()) :: list()
  @spec list_overlap(list(), list(), list()) :: list()

  @doc """
  Part 1: Check rucksack overlaps.

  ## Examples

    iex> Days.Day03.pt1(day03_input) # filename
    <Solution to Day 3, part 1>

  """
  def pt1(file_name) do
    score = &(prio(shared_item(&1)))
    File.stream!(file_name)
      |> Stream.map(&String.trim/1)
      |> Enum.reduce(0, &(score.(&1) + &2))
  end

  defp prio(item) do
    cond do
      item in 97..122 -> item - 96
      item in 65..90 -> item - 38
      true -> raise "invalid item: #{item}"
    end
  end

  @doc """
  Part 2: Check group-of-three overlap.

  ## Examples

    iex> Days.Day03.pt2(day03_input) # filename
    <Solution to Day 3, part 2>

  """
  def pt2(file_name) do
    score = fn [r1, r2, r3] -> prio(hd(list_overlap(r1, r2, r3))) end
    File.stream!(file_name)
      |> Stream.map(&String.trim/1)
      |> Stream.map(&String.to_charlist/1)
      |> Stream.chunk_every(3)
      |> Enum.reduce(0, &(score.(&1) + &2))
  end

  # --------------- Private Functions --------------- #

  defp shared_item(rucksack) do
    rucksack
      |> String.to_charlist
      # split the rucksack in half
      # should maybe directly split string/binary
      # with String.split_at/2 or binary_part/3
      |> split_list()
      |> then(fn {l1, l2} -> list_overlap(l1, l2) end)
      |> hd()
  end

  defp split_list(list) do
    mid = round(length(list)/2)
    Enum.split(list, mid)
  end

  defp list_overlap(l1, l2) do
    in_l1 = MapSet.new(l1)
    Enum.filter(l2, &(MapSet.member?(in_l1, &1)))
  end

  defp list_overlap(l1, l2, l3) do
    list_overlap(list_overlap(l1, l2), l3)
  end

  # How to get unique elements of a list:
  # list
  #   |> (&(&1 -- Enum.uniq(&1))).()
  #   |> Enum.uniq
end
