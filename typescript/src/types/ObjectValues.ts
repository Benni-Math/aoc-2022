/**
 * Type for getting the typeof values of an object.
 * @author Benedikt Arnarsson
 */
type ObjectValues<T> = T[keyof T];

export default ObjectValues;
