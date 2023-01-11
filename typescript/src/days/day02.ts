// Import NodeJS helpers
import fs from 'fs';

// Import types
import InputFile from '../types/InputFile';

// ----------------- Helpers ----------------- //

const wrongRPSScore = (game: string): number => {
  if (game === 'A X') return 4;
  if (game === 'A Y') return 8;
  if (game === 'A Z') return 3;
  if (game === 'B X') return 1;
  if (game === 'B Y') return 5;
  if (game === 'B Z') return 9;
  if (game === 'C X') return 7;
  if (game === 'C Y') return 2;
  if (game === 'C Z') return 6;
  return 0;
};

const rightRPSScore = (game: string): number => {
  if (game === 'A X') return 3;
  if (game === 'A Y') return 4;
  if (game === 'A Z') return 8;
  if (game === 'B X') return 1;
  if (game === 'B Y') return 5;
  if (game === 'B Z') return 9;
  if (game === 'C X') return 2;
  if (game === 'C Y') return 6;
  if (game === 'C Z') return 7;
  return 0;
};

// ------------- Main Functions -------------- //

/**
 * Day 2 Pt1 of Advent of Code 2022!
 * Scoring rock-paper-scissors games, the wrong way.
 * @author Benedikt Arnarsson
 */
const pt1 = async (filename: InputFile) => {
  const inputFile = await fs.promises.readFile(filename);

  const totalScore = inputFile
    .toString()
    .trim()
    .split('\n')
    .reduce((sum, game) => wrongRPSScore(game) + sum, 0);

  return totalScore;
};

/**
 * Day 2 Pt2 of Advent of Code 2022!
 * Scoring rock-paper-scissors games, the right way.
 * @author Benedikt Arnarsson
 */
const pt2 = async (filename: InputFile) => {
  const inputFile = await fs.promises.readFile(filename);

  const totalScore = inputFile
    .toString()
    .split('\n')
    .reduce((sum, game) => rightRPSScore(game) + sum, 0);

  return totalScore;
};

const day02 = [pt1, pt2];

export default day02;
