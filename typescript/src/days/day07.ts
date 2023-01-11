// Import NodeJS helpers
import fs from 'fs';

// Import types
import InputFile from '../types/InputFile';

// ------------------ Types ------------------ //

type FileSystem = {
  currDir: string,
  directories: Directories,
};

// type Directories = {
//   [k: string]: number,
// };

type Directories = Map<string, number>;

// ----------------- Helpers ----------------- //

const newFileSystem = (): FileSystem => {
  const currDir = '/';
  const directories = new Map([['/', 0]]);

  return {
    currDir,
    directories,
  };
};

const changeDir = (fileSystem: FileSystem, dirName: string): FileSystem => {
  const {
    currDir,
    directories,
  } = fileSystem;
  if (dirName === '..' && currDir !== '/') {
    const nextDir = currDir
      .split('/')
      .slice(0, -2)
      .join('/');
    return {
      currDir: `${nextDir}/`,
      directories,
    };
  }
  if (dirName === '/') {
    return {
      currDir: '/',
      directories,
    };
  }
  return {
    currDir: `${currDir}${dirName}/`,
    directories,
  };
};

const addDir = (fileSystem: FileSystem, dirName: string): FileSystem => {
  const {
    currDir,
    directories,
  } = fileSystem;

  directories.set(`${currDir}${dirName}/`, 0);

  return {
    currDir,
    directories,
  };
};

const addFile = (fileSystem: FileSystem, fileSize: number): FileSystem => {
  const {
    currDir,
    directories,
  } = fileSystem;

  const dirSteps = currDir
    .replaceAll('/', '/,')
    .split(',')
    .slice(0, -1);

  dirSteps.reduce(
    (dir, next) => {
      const nextDir = dir + next;
      const currSize = directories.get(nextDir);
      directories.set(nextDir, currSize + fileSize);
      return nextDir;
    },
    '',
  );

  return {
    currDir,
    directories,
  };
};

const parseLine = (fileSystem: FileSystem, line: string): FileSystem => {
  const cmds = line.split(' ');

  if (cmds[0] === '$' && cmds[1] === 'cd') {
    return changeDir(fileSystem, cmds[2]);
  }
  if (cmds[0] === 'dir') {
    return addDir(fileSystem, cmds[1]);
  }
  const fileSize = Number.parseInt(cmds[0], 10);
  if (!Number.isNaN(fileSize)) {
    return addFile(fileSystem, fileSize);
  }

  return fileSystem;
};

const sumOfSmall = (fileSystem: FileSystem, sizeLimit = 100_000): number => {
  const { directories } = fileSystem;

  let sum = 0;
  for (const dirSize of directories.values()) {
    if (dirSize <= sizeLimit) sum += dirSize;
  }
  return sum;
};

const minDirToDelete = (fileSystem: FileSystem, totalSpace = 70_000_000, spaceNeeded = 30_000_000): number => {
  const { directories } = fileSystem;

  const spaceTaken = directories.get('/');

  const toRemove = spaceNeeded - (totalSpace - spaceTaken);

  let min = totalSpace;
  for (const dirSize of directories.values()) {
    if (dirSize >= toRemove && dirSize < min) min = dirSize;
  }

  return min;
};

// ------------- Main Functions -------------- //

/**
 * Day 7 Pt1 of Advent of Code 2022: No Space Left On Device!
 * Get the sum of the small directories.
 * @author Benedikt Arnarsson
 */
const pt1 = async (filename: InputFile) => (
  fs.promises
    .readFile(filename)
    .then((buf) => buf.toString())
    .then((str) => str.split('\n'))
    .then((lines) => lines.reduce(parseLine, newFileSystem()))
    .then(sumOfSmall)
);

/**
 * Day 7 Pt2 of Advent of Code 2022: No Space Left On Device!
 * Get the size of the smallest directory to delete.
 * @author Benedikt Arnarsson
 */
const pt2 = async (filename: InputFile) => (
  fs.promises
    .readFile(filename)
    .then((buf) => buf.toString())
    .then((str) => str.split('\n'))
    .then((lines) => lines.reduce(parseLine, newFileSystem()))
    .then(minDirToDelete)
);

const day07 = [pt1, pt2];

export default day07;
