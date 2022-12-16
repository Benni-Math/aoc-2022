use std::fs::File;
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };


struct SumMax {
    max: u64,
    sum: u64,
}

pub fn day01_pt1(filename: &PathBuf) -> std::io::Result<u64> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(
            SumMax { max: 0, sum: 0 },
            |sum_max, line| {
                let SumMax { max: curr_max, sum: curr_sum } = sum_max;
                match line.as_str() {
                    "" => SumMax {
                        max: if curr_sum > curr_max { curr_sum } else { curr_max },
                        sum: 0,

                    },
                    s => SumMax {
                        max: curr_max,
                        sum: curr_sum + s.parse::<u64>().unwrap()
                    } 
                }
            }
        )
        .max;

    Ok(answer)
}
