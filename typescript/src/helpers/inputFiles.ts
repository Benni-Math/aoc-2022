// Import constants
import INPUT_DIR from '../constants/INPUT_DIR';

/**
 * Function for getting all the input file names.
 * @author Benedikt Arnarsson
 */
const inputFiles = () => (
  [...Array(25).keys()]
    .map((index) => index + 1)
    .map((index) => `${index}` as const)
    .map((num) => (num.length === 2 ? num : `0${num}` as const))
    .map((filename) => `${INPUT_DIR}/${filename}.txt` as const)
);

export default inputFiles;
