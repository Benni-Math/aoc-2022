// Import NodeJS helpers
import fs from 'fs';
import readline from 'readline';

// Import types
import InputFile from '../types/InputFile';

/**
 * Day 1 Pt1 of Advent of Code 2022!
 * @author Benedikt Arnarsson
 */
const pt1 = async (filename: InputFile) => {
  const inputFile = fs.createReadStream(filename);

  const lineReader = readline.createInterface({
    input: inputFile,
    crlfDelay: Infinity,
  });

  let sum = 0;
  let max = 0;
  for await (const line of lineReader) {
    if (line === '') {
      max = sum > max ? sum : max;
      sum = 0;
    } else {
      sum += Number.parseInt(line, 10);
    }
  }

  return max;
};

const pt2 = async (filename: InputFile) => {
  const inputFile = fs.createReadStream(filename);

  const lineReader = readline.createInterface({
    input: inputFile,
    crlfDelay: Infinity,
  });

  let sum = 0;
  const threeMax = [0, 0, 0];
  for await (const line of lineReader) {
    if (line === '') {
      if (sum > threeMax[0]) {
        threeMax[0] = sum;
        threeMax.sort();
      }
      sum = 0;
    } else {
      sum += Number.parseInt(line, 10);
    }
  }

  return threeMax.reduce((x, y) => x + y, 0);
};

const day01 = [pt1, pt2];

export default day01;
