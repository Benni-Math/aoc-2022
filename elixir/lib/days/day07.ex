defmodule Days.Day07 do
  @moduledoc """
  Solutions to AoC 2022 Day 7: No Space Left On Device.
  """

  # Public Functions
  @spec pt1(binary()) :: integer()
  @spec pt2(binary()) :: integer()

  # Types
  @typep filesystem :: %{binary() => integer(), curr_dir: binary()}

  # Private Functions
  @spec parse_line(binary(), filesystem()) :: filesystem()
  @spec change_dir(filesystem(), binary()) :: filesystem()
  @spec add_dir(filesystem(), binary()) :: filesystem()
  @spec add_file(filesystem(), integer()) :: filesystem()

  @doc """
  Part 1: Sum of small directories.

  ## Examples

    iex> Days.Day07.pt1(day07_input) # filename
    <Solution to Day 7, part 1>

  """
  def pt1(file_name) do
    fs = %{"/" => 0, curr_dir: ""}

    File.stream!(file_name)
      |> Stream.map(&(String.trim(&1, "\n")))
      |> Enum.reduce(fs, &parse_line/2)
      |> Map.delete(:curr_dir)
      |> Map.values
      |> Enum.reduce(0, fn size, sum ->
        if size < 100_000 do
          sum + size
        else
          sum
        end
      end)
  end

  @doc """
  Part 2: Smallest directory to delete.

  ## Examples

    iex> Days.Day07.pt2(day07_input) # filename
    <Solution to Day 7, part 2>

  """
  def pt2(file_name) do
    fs = %{"/" => 0, curr_dir: ""}

    File.stream!(file_name)
      |> Stream.map(&(String.trim(&1, "\n")))
      |> Enum.reduce(fs, &parse_line/2)
      |> Map.delete(:curr_dir)
      |> (fn dirs -> {dirs, dirs["/"]} end).()
      |> (fn {dirs, total_size} -> {Map.values(dirs),  total_size - 40_000_000} end).()
      |> (fn {sizes, space_to_free} -> Enum.filter(sizes, &(&1 >= space_to_free)) end).()
      |> Enum.min()
  end

  # --------------- Private Functions --------------- #

  defp parse_line(line, fs) do
    case String.split(line) do
      ["$", "cd", dir] -> change_dir(fs, dir)
      ["$", "ls"] -> fs
      ["dir", dir] -> add_dir(fs, dir)
      [size, _file_name] -> add_file(fs, String.to_integer(size))
      _ -> raise "Malformed input: #{line}"
    end
  end

  defp change_dir(fs, path) do
    curr_dir = fs.curr_dir
    case path do
      ".." ->
        unless curr_dir == "/" do
          next_dir = curr_dir |> String.split("/") |> Enum.drop(-2) |> Enum.join("/")
          Map.replace(fs, :curr_dir, next_dir <> "/")
        else
          fs
        end
      "/" -> Map.replace(fs, :curr_dir, "/")
      dir -> Map.replace(fs, :curr_dir, curr_dir <> dir <> "/" )
    end
  end

  defp add_dir(fs, dir) do
    Map.put_new(fs, fs.curr_dir <> dir <> "/", 0)
  end

  defp add_file(fs, size) do
    fs.curr_dir
      |> String.split("/")
      |> Enum.drop(-1)
      |> Enum.reduce({"", fs}, fn next_path, {path, curr_fs} ->
        curr_dir = path <> next_path <> "/"
        curr_size = curr_fs[curr_dir]
        if curr_size do
          {curr_dir, Map.put(curr_fs, curr_dir, curr_size + size)}
        else
          {curr_dir, curr_fs}
        end
      end)
      |> elem(1)
  end
end
