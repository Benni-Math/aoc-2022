// Import NodeJS helpers
import fs from 'fs';
import readline from 'readline';

// Import types
import InputFile from '../types/InputFile';

// Import constants
import INPUT_FILE from '../constants/INPUT_FILE';

// Import helpers
import RockPaperScissors from '../types/RockPaperScissors';

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
  for await (const line of lineReader) {
    const game = RockPaperScissors.fromString(line as RockPaperScissors.GameStr);
    sum += RockPaperScissors.score(game);
  }

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

const day02 = [pt1, pt2];

export default day02;
