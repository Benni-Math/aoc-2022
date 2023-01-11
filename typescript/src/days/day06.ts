// Import NodeJS helpers
import fs from 'fs';

// Import types
import InputFile from '../types/InputFile';

// ----------------- Helpers ----------------- //

const uniqueStr = (str: string): boolean => {
  const charMap = new Map<string, boolean>();

  for (let i = 0; i < str.length; i++) {
    const char = str.charAt(i);
    if (charMap.has(char)) return false;
    charMap.set(char, true);
  }
  return true;
};

const findUniqueSub = (str: string, subLen: number): number => {
  for (let i = 0; i < str.length - subLen; i++) {
    if (uniqueStr(str.slice(i, i + subLen))) return i + subLen;
  }
  return str.length;
};

// ------------- Main Functions -------------- //

/**
 * Day 6 Pt1 of Advent of Code 2022!
 * @author Benedikt Arnarsson
 */
const pt1 = async (filename: InputFile) => {
  const inputFile = await fs.promises.readFile(filename);

  return findUniqueSub(inputFile.toString(), 4);
};

/**
 * Day 6 Pt2 of Advent of Code 2022!
 * @author Benedikt Arnarsson
 */
const pt2 = async (filename: InputFile) => {
  const inputFile = await fs.promises.readFile(filename);

  return findUniqueSub(inputFile.toString(), 14);
};

const day06 = [pt1, pt2];

export default day06;
