defmodule Days.Day08 do
  @moduledoc """
  Solutions to AoC 2022 Day 8: Treetop Tree House.
  """

  # Public Functions
  @spec pt1(binary()) :: integer()
  @spec pt2(binary()) :: integer()

  @doc """
  Part 1: How many trees are visible from outside?

  ## Examples

    iex> Days.Day08.pt1(day08_input) # filename
    <Solution to Day 8, part 1>

  """
  def pt1(file_name) do
    # I want to make a matrix,
    # but that wouldn't be very efficient,
    # and it doesn't seem like the 'Elixir'
    # way of doing things...

    # I want to make into a list(list(integer()))
    # and then spin up multiple processes to calculate each
    IO.puts file_name
    0
  end

  @doc """
  Part 2: ???

  ## Examples

    iex> Days.Day08.pt2(day08_input) # filename
    <Solution to Day 8, part 2>

  """
  def pt2(file_name) do
    String.length file_name
  end

  # --------------- Private Functions --------------- #
end
