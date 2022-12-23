use std::fs::File;
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };

use crate::util::collect_array;
struct Range (u64, u64);

impl Range {
    fn parse(s: &str) -> Result<Range, std::num::ParseIntError> {
        let [low, high] = collect_array(s.split('-'));

        Ok(Range (low.parse()?, high.parse()?))
    }
}

fn check_containment(elf1: Range, elf2: Range) -> bool {
    (elf1.0 <= elf2.0 && elf2.1 <= elf1.1)      // elf2 \subset elf1
    || (elf2.0 <= elf1.0 && elf1.1 <= elf2.1)   // elf1 \subset elf2
}

fn check_overlap(elf1: Range, elf2: Range) -> bool {
    (elf1.0 <= elf2.0 && elf2.0 <= elf1.1)
    || (elf2.0 <= elf1.0 && elf1.0 <= elf2.1)
}

pub fn pt1(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(0, |sum, pair| {
            let [Ok(elf1), Ok(elf2)] = collect_array(pair.split(','))
                .map(Range::parse) 
                else { panic!("Malformed pair: {}", pair) };
            if check_containment(elf1, elf2) 
                { sum + 1 }
            else 
                { sum }
        });

    Ok(format!("{}", answer))
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(0, |sum, pair| {
            let [Ok(elf1), Ok(elf2)] = collect_array(pair.split(','))
                .map(Range::parse) 
                else { panic!("Malformed pair: {}", pair) };
            if check_overlap(elf1, elf2) 
                { sum + 1 }
            else 
                { sum }
        });

    Ok(format!("{}", answer))
}