defmodule Days.Day02 do
  @moduledoc """
  Solutions to AoC 2022 Day 2: Rock Paper Scissors.
  """

  # Public Functions
  @spec pt1(binary()) :: integer()
  @spec pt2(binary()) :: integer()

  # Private Functions
  @spec wrong_rps_score(binary()) :: integer()
  @spec right_rps_score(binary()) :: integer()

  @doc """
  Part 1: Find rock-paper-scissors score (the wrong way).

  ## Examples

    iex> Days.Day02.pt1(day02_input) # filename
    <Solution to Day 2, part 1>

  """
  def pt1(file_name) do
    File.stream!(file_name)
      |> Stream.map(&String.trim/1)
      |> Enum.reduce(0, &(wrong_rps_score(&1) + &2))
  end

  @doc """
  Part 2: Find rock-paper-scissors score (the right way).

  ## Examples

    iex> Days.Day02.pt2(day02_input) # filename
    <Solution to Day 2, part 2>

  """
  def pt2(file_name) do
    File.stream!(file_name)
      |> Stream.map(&String.trim/1)
      |> Enum.reduce(0, &(right_rps_score(&1) + &2))
  end

  # --------------- Private Functions --------------- #

  defp wrong_rps_score(game) do
    case game do
      "A X" -> 4 # Rock, Rock
      "A Y" -> 8 # Rock, Paper
      "A Z" -> 3 # Rock, Scissors
      "B X" -> 1 # Paper, Rock
      "B Y" -> 5 # Paper, Paper
      "B Z" -> 9 # Paper, Scissors
      "C X" -> 7 # Scissors, Rock
      "C Y" -> 2 # Scissors, Paper
      "C Z" -> 6 # Scissors, Scissors
      _ -> raise "Malformed game: #{game}"
    end
  end

  defp right_rps_score(game) do
    case game do
      "A X" -> 3 # Rock, Rock
      "A Y" -> 4 # Rock, Paper
      "A Z" -> 8 # Rock, Scissors
      "B X" -> 1 # Paper, Rock
      "B Y" -> 5 # Paper, Paper
      "B Z" -> 9 # Paper, Scissors
      "C X" -> 2 # Scissors, Rock
      "C Y" -> 6 # Scissors, Paper
      "C Z" -> 7 # Scissors, Scissors
      _ -> raise "Malformed game: #{game}"
    end
  end
end
