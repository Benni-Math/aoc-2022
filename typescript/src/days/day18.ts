// Import NodeJS helpers
import fs from 'fs';

// Import types
import InputFile from '../types/InputFile';

// ----------------- Helpers ----------------- //

// ------------- Main Functions -------------- //

/**
 * Day 18Pt1 of Advent of Code 2022!
 * @author Benedikt Arnarsson
 */
const pt1 = async (filename: InputFile) => {
  const inputFile = await fs.promises.readFile(filename);

  return 0;
};

/**
 * Day 18 Pt2 of Advent of Code 2022!
 * @author Benedikt Arnarsson
 */
const pt2 = async (filename: InputFile) => {
  const inputFile = await fs.promises.readFile(filename);

  return 0;
};

const day18 = [pt1, pt2];

export default day18;
