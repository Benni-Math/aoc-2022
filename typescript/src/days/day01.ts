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
const day01pt1 = async (filename: InputFile) => {
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

if (require.main === module) {
  day01pt1(INPUT_FILE.DAY_1).then((answer) => {
    console.log(`Day 1, pt1: ${answer}`);
  });
}

const day01 = [day01pt1];

export default day01;
