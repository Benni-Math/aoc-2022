// Import NodeJS helpers
import fs from 'fs';

// Import types
import InputFile from '../types/InputFile';

// ------------------ Types ------------------ //

type Range = {
  low: number,
  high: number,
};

// ----------------- Helpers ----------------- //
/**
 * Parse a string into a Range.
 * @author Benedikt Arnarsson
 * @param str Must be of the form `${number}-${number}`
 */
const parseRange = (str: `${number}-${number}`): Range => {
  const [low, high] = str
    .split('-')
    .map((s) => Number.parseInt(s, 10));

  return { low, high };
};

const rangeContainment = (ranges: Range[]): boolean => (
  (ranges[0].low <= ranges[1].low && ranges[1].high <= ranges[0].high)
  || (ranges[1].low <= ranges[0].low && ranges[0].high <= ranges[1].high)
);

const rangeOverlap = (ranges: Range[]): boolean => (
  (ranges[0].low <= ranges[1].low && ranges[1].low <= ranges[0].high)
  || (ranges[1].low <= ranges[0].low && ranges[0].low <= ranges[1].high)
);

// ------------- Main Functions -------------- //

/**
 * Day 4 Pt1 of Advent of Code 2022!
 * Camp Cleanup: How many elves' cleanup areas are contained in each other?
 * @author Benedikt Arnarsson
 */
const pt1 = async (filename: InputFile) => (
  fs.promises
    .readFile(filename)
    .then((buf) => buf.toString())
    .then((str) => str.trim().split('\n'))
    .then((lines) => lines.map((line) => line.split(',').map(parseRange)))
    .then((ranges) => ranges.filter(rangeContainment).length)
);

/**
 * Day 4 Pt2 of Advent of Code 2022!
 * Camp Cleanup: How many elves' cleanup areas overlap?
 * @author Benedikt Arnarsson
 */
const pt2 = async (filename: InputFile) => (
  fs.promises
    .readFile(filename)
    .then((buf) => buf.toString())
    .then((str) => str.trim().split('\n'))
    .then((lines) => lines.map((line) => line.split(',').map(parseRange)))
    .then((ranges) => ranges.filter(rangeOverlap).length)
);

const day04 = [pt1, pt2];

export default day04;
