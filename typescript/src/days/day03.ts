// Import NodeJS helpers
import fs from 'fs';

// Import types
import InputFile from '../types/InputFile';

// ----------------- Helpers ----------------- //

const splitRucksack = (rucksack: string): [string, string] => {
  const mid = rucksack.length / 2;
  return [rucksack.slice(0, mid), rucksack.slice(mid)];
};

const rucksackOverlap = (rucksacks: [string, string]): string => {
  const ruckMap = new Map<string, boolean>();

  [...rucksacks[0]].forEach((char) => ruckMap.set(char, true));

  return [...rucksacks[1]].find((char) => ruckMap.has(char));
};

const splitGroups = (rucksacks: string[]): string[][] => {
  const groups = [];

  for (let i = 0; i < rucksacks.length - 3; i += 3) {
    groups.push([
      rucksacks[i],
      rucksacks[i + 1],
      rucksacks[i + 2],
    ]);
  }

  return groups;
};

const groupOverlap = (group: string[]): string => {
  const ruckMap = new Map<string, boolean>();

  [...group[0]].forEach((char) => ruckMap.set(char, false));

  [...group[1]].forEach((char) => (
    ruckMap.has(char)
      ? ruckMap.set(char, true)
      : null
  ));

  return [...group[2]].find((char) => ruckMap.has(char) && ruckMap.get(char));
};

const priority = (char: string) => {
  if (!char) return 0;

  const ord = char.charCodeAt(0);

  if (ord > 96 && ord < 123) return ord - 96;
  if (ord > 64 && ord < 91) return ord - 38;
};

// ------------- Main Functions -------------- //

/**
 * Day 3 Pt1 of Advent of Code 2022!
 * Given a list of pairs of rucksacks, what items do the pairs share?
 * @author Benedikt Arnarsson
 */
const pt1 = async (filename: InputFile) => {
  const inputFile = await fs.promises.readFile(filename);

  return inputFile
    .toString()
    .split('\n')
    .map(splitRucksack)
    .map(rucksackOverlap)
    .map(priority)
    .reduce((sum, nxt) => sum + nxt, 0);
};

/**
 * Day 3 Pt2 of Advent of Code 2022!
 * Given groups-of-three, what item does each group share?
 * @author Benedikt Arnarsson
 */
const pt2 = async (filename: InputFile) => {
  const inputFile = await fs.promises.readFile(filename);

  const rucksacks = inputFile.toString().split('\n');
  const groups = splitGroups(rucksacks);

  return groups
    .map(groupOverlap)
    .map(priority)
    .reduce((sum, nxt) => sum + nxt, 0);
};

const day03 = [pt1, pt2];

export default day03;
