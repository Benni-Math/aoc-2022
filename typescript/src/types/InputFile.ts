// Import types
import ObjectValues from './ObjectValues';

// Import constants
import INPUT_FILE from '../constants/INPUT_FILE';

/**
 * Enum style type to keep track of input files.
 * @author Benedikt Arnarsson
 */
type InputFile = ObjectValues<typeof INPUT_FILE>;

export default InputFile;
