// Import NodeJS helpers
import fs from 'fs';
import readline from 'readline';

// Import types
import InputFile from '../types/InputFile';

// Import constants
import INPUT_FILE from '../constants/INPUT_FILE';

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

if (require.main === module) {
  pt1(INPUT_FILE.DAY_1)
    .then((answer) => {
      console.log(`Day 1, pt1: ${answer}`);
    });

  pt2(INPUT_FILE.DAY_1)
    .then((answer) => {
      console.log(`Day 1, pt2: ${answer}`);
    });
}

const day01 = [pt1, pt2];

export default day01;
