use std::fs::File;
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };

use crate::util::get_index_of_lowest;

struct SumMax {
    sum: u64,
    max: u64,
}

struct SumTMax<const T: usize> {
    sum: u64,
    max: [u64; T],
    total: u64,
}

pub fn pt1(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(
            SumMax { sum: 0, max: 0 },
            |sum_max, line| {
                let SumMax { sum: curr_sum, max: curr_max } = sum_max;
                match line.as_str() {
                    "" => SumMax {
                        sum: 0,
                        max: if curr_sum > curr_max { curr_sum } else { curr_max },
                    },
                    s => SumMax {
                        sum: curr_sum + s.parse::<u64>().unwrap(),
                        max: curr_max,
                    } 
                }
            }
        )
        .max;

    Ok(format!("{}", answer))
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(
            SumTMax { sum: 0, max: [0, 0, 0], total: 0 },
            |s, line| {
                match line.as_str() {
                    "" => {
                        let lowest = get_index_of_lowest(&s.max);
                        let new_max = if s.sum > s.max[lowest] {
                            let mut inter = s.max;
                            inter[lowest] = s.sum;
                            inter
                        } else {
                            s.max
                        };
                        let new_total = new_max.iter().sum();
                        SumTMax {
                            sum: 0,
                            max: new_max,
                            total: new_total,
                        }
                    },
                    num_str => SumTMax {
                        sum: s.sum + num_str.parse::<u64>().unwrap(),
                        max: s.max,
                        total: s.total,
                    } 
                }
            }
        )
        .total;

    Ok(format!("{}", answer))
}