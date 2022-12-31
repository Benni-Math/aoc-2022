// Import NodeJS helpers
import fs from 'fs';
import readline from 'readline';

// Import types
import InputFile from '../types/InputFile';

// Import constants
import INPUT_FILE from '../constants/INPUT_FILE';

/**
 * Day 3 Pt1 of Advent of Code 2022!
 * @author Benedikt Arnarsson
 */
const pt1 = async (filename: InputFile) => {
  const inputFile = fs.createReadStream(filename);

  const lineReader = readline.createInterface({
    input: inputFile,
    crlfDelay: Infinity,
  });

  const sum = 0;

  return sum;
};

const pt2 = async (filename: InputFile) => 0;

if (require.main === module) {
  pt1(INPUT_FILE.DAY_2)
    .then((answer) => {
      console.log(`Day 2, pt1: ${answer}`);
    });

  pt2(INPUT_FILE.DAY_2)
    .then((answer) => {
      console.log(`Day 2, pt2: ${answer}`);
    });
}

const day03 = [pt1, pt2];

export default day03;
