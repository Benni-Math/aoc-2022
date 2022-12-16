use std::fs::File;
use std::io::{ BufReader, BufRead };


const INPUT_FILENAME: &str = "../inputs/day01-input.txt";

struct SumMax {
    max: u64,
    sum: u64,
}

pub fn day01() -> std::io::Result<()> {
    let file = File::open(INPUT_FILENAME)?;
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

    println!("Day 1 Part 1: {}", answer);

    
    Ok(())
}
