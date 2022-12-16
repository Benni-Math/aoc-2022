import ObjectValues from './ObjectValues';

const INPUT_DIR = '../inputs/';

/**
 * Enum-style type and object to keep track of input files.
 * @author Benedikt Arnarsson
 */
const INPUT_FILE = {
  DAY_1: `${INPUT_DIR}day01-input.txt`,
} as const;

export type InputFile = ObjectValues<typeof INPUT_FILE>;

export default INPUT_FILE;
