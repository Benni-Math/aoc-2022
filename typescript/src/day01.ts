// Import NodeJS helpers
import fs from 'fs';
import readline from 'readline';

// Import input file information
import INPUT_FILE from './types/InputFile';

/**
 * Day 1 of Advent of Code 2022!
 * @author Benedikt Arnarsson
 */
const day01 = async () => {
  const inputFile = fs.createReadStream(INPUT_FILE.DAY_1);

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

  // eslint-disable-next-line no-console
  console.log(max);
};

if (require.main === module) {
  day01();
}
