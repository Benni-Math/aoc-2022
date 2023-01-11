use std::fs::File;
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };

pub fn pt1(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten();

    Ok("Not implemented".to_string())
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten();

    Ok("Not implemented".to_string())
}