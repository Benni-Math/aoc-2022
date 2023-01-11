// Import NodeJS helpers
import fs from 'fs';

// Import types
import InputFile from '../types/InputFile';

// ------------------ Types ------------------ //

type SupplyStacks = string[][];

type CraneMove = {
  numCrates: number,
  from: number,
  to: number,
};

// ----------------- Helpers ----------------- //

const splitInput = async (filename: InputFile) => {
  const inputFile = await fs.promises.readFile(filename);
  const [revCrates, moves] = inputFile
    .toString()
    .split('\n\n')
    .map((str) => str.split('\n'))
    .map((list) => { list.pop(); return list; });

  const crates = revCrates.reverse();

  return {
    crates,
    moves,
  };
};

const parseRow = (row: string) => {
  const crateRow: string[] = [];
  for (let i = 1; i < row.length; i += 4) {
    crateRow.push(row.charAt(i));
  }

  return crateRow;
};

const initSupplyStacks = (rows: string[]): SupplyStacks => {
  const numRows = (rows[0].length + 1) / 4;
  const supplyStacks: SupplyStacks = Array(numRows)
    .fill('')
    .map((s) => [s]);

  rows
    .map(parseRow)
    .forEach((row) => (
      row.forEach((crate, col) => {
        if (crate === ' ') return;
        supplyStacks[col].push(crate);
      })
    ));

  return supplyStacks;
};

const parseMove = (moveStr: string): CraneMove => {
  const moveList = moveStr
    .split(' ')
    .map((str) => Number.parseInt(str, 10))
    .filter((num) => !Number.isNaN(num));

  return {
    numCrates: moveList[0],
    from: moveList[1] - 1,
    to: moveList[2] - 1,
  };
};

const crateMover9000 = (supplyStacks: SupplyStacks, move: CraneMove): SupplyStacks => {
  const newSupplyStacks = supplyStacks;
  const {
    numCrates,
    from,
    to,
  } = move;

  for (let i = 0; i < numCrates; i++) {
    newSupplyStacks[to].push(newSupplyStacks[from].pop());
  }

  return newSupplyStacks;
};

const crateMover9001 = (supplyStacks: SupplyStacks, move: CraneMove): SupplyStacks => {
  const newSupplyStacks = supplyStacks;
  const {
    numCrates,
    from,
    to,
  } = move;

  const cratesToMove = newSupplyStacks[from].splice(-numCrates, numCrates);

  newSupplyStacks[to] = newSupplyStacks[to].concat(cratesToMove);

  return newSupplyStacks;
};

// ------------- Main Functions -------------- //

/**
 * Day 5 Pt1 of Advent of Code 2022!
 * Results according to the Crate Mover 9000.
 * @author Benedikt Arnarsson
 */
const pt1 = async (filename: InputFile) => {
  const {
    crates,
    moves,
  } = await splitInput(filename);

  const supplyStacks = initSupplyStacks(crates);

  return moves
    .map(parseMove)
    .reduce(crateMover9000, supplyStacks)
    .map((col) => col.pop())
    .join('');
};

/**
 * Day 5 Pt2 of Advent of Code 2022!
 * Results according to the Crate Mover 9001.
 * @author Benedikt Arnarsson
 */
const pt2 = async (filename: InputFile) => {
  const {
    crates,
    moves,
  } = await splitInput(filename);

  const supplyStacks = initSupplyStacks(crates);

  return moves
    .map(parseMove)
    .reduce(crateMover9001, supplyStacks)
    .map((col) => col.pop())
    .join('');
};

const day05 = [pt1, pt2];

export default day05;
