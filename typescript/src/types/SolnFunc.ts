// Import types
import InputFile from './InputFile';

/**
 * Type describing a function solving an AoC part.
 * @author Benedikt Arnarsson
 */
type SolnFunc = (filename: InputFile) => Promise<number | string>;

export default SolnFunc;
