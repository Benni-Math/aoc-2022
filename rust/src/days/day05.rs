use std::collections::VecDeque;
use std::fs::{File, create_dir};
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };

use crate::util::collect_array;

type CrateRow = Vec<Option<char>>;

struct CrateStacks {
    stacks: VecDeque<CrateRow>,
    crane_moves: Box<dyn Iterator<Item = String>>,
}

struct CraneMove {
    num: usize,
    from: usize,
    to: usize,
}

impl CrateStacks {
    pub fn new(mut lines: Box<dyn Iterator<Item = String>>) -> Self {
        let crate_stack_rows = CrateStacks::parse_crates(&mut lines);
        CrateStacks { stacks: crate_stack_rows, crane_moves: lines }
    }

    fn parse_crates(lines: &mut dyn Iterator<Item = String>) -> VecDeque<CrateRow> {
        let mut crate_stack_rows = VecDeque::new();
        for row in lines {
            if row.is_empty() { break; }
            let crate_row = row
                .chars()
                .collect::<Vec<char>>();
            let crate_names = crate_row
                .chunks(4)
                .map(|name| {
                    name
                        .iter()
                        .find(|c| { c.is_alphabetic() })
                        .map(|c| { c.to_owned() })
                });
            crate_stack_rows.push_back(crate_names.collect())
        }
        crate_stack_rows.pop_back();
        crate_stack_rows
    }

    pub fn exec_all_crane(self) -> String {
        let mut new_crate_stacks = self.stacks;
        for line in self.crane_moves {
            let crane_move = CrateStacks::parse_crane_move(&line);
            new_crate_stacks = CrateStacks::exec_crane(new_crate_stacks, crane_move);
        }

        // FIXME: only get the last row, not the top of each stack
        // could do get_top_of_col, but might want to change CrateStacks::new()
        // to use a stack for each row
        // This would also simplify the structure of move_one
        // Maybe just have something that changes VecDeque<CrateRow> into
        // the set of stacks
        let mut answer = String::new();
        for col in 0..new_crate_stacks[0].len() {
            if let Some(row) = CrateStacks::get_top_of_col(&new_crate_stacks, col) {
                answer.push(new_crate_stacks[row][col].unwrap())
            }
        }

        println!("Crates: {:?}", new_crate_stacks);

        answer
        // if let Some(last_row) =  new_crate_stacks.pop_front() {
        //     last_row.iter().filter_map(|c| { c.as_ref() }).collect()
        // } else { panic!("Empty crate stacks: {:?}", new_crate_stacks) }
    } 

    fn exec_crane(crate_rows: VecDeque<CrateRow>, crane_move: CraneMove) -> VecDeque<CrateRow> {
        let mut new_crate_rows = crate_rows;
        for _ in 0..crane_move.num {
            new_crate_rows = CrateStacks::move_one(new_crate_rows, crane_move.from-1, crane_move.to-1);
        }

        new_crate_rows
    }

    fn move_one(crate_rows: VecDeque<CrateRow>, from: usize, to: usize) -> VecDeque<CrateRow> {
        let mut new_crate_rows = crate_rows;
        
        let Some(from_row) = CrateStacks::get_top_of_col(&new_crate_rows, from) 
            else { return new_crate_rows; };

        let to_row = CrateStacks::get_top_of_col(&new_crate_rows, to);

        match to_row {
            Some(i) if i == new_crate_rows.len()-1 => {
                let len = new_crate_rows[0].len();
                let mut none_vec = vec![None; len];
                none_vec[to] = new_crate_rows[from_row][from];
                new_crate_rows.push_front(none_vec);
            },
            Some(i) => {
                new_crate_rows[i + 1][to] = new_crate_rows[from_row][from];
            }
            None => {
                new_crate_rows[0][to] = new_crate_rows[from_row][from];
            }
        }
        
        new_crate_rows
    }

    fn get_top_of_col(crate_rows: &VecDeque<CrateRow>, col: usize) -> Option<usize> {
        (0..crate_rows.len()).rev().find(|&i| crate_rows[i][col].is_some())
    }

    fn parse_crane_move(s: &str) -> CraneMove {
        let [_, num, _, from, _, to] = collect_array(s.split(' '));
        match [num, from, to].map(|s| { s.parse::<usize>() }) {
            [Ok(num), Ok(from), Ok(to)] => CraneMove {
                num,
                from,
                to,
            },
            _ => panic!("Malformed crane move: {}", s),
        }
    }
}



pub fn pt1(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let lines = reader
        .lines()
        .flatten();
    
    let crate_stacks = CrateStacks::new(Box::new(lines));
    let answer = crate_stacks.exec_all_crane();
    Ok(answer)
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten();

    Ok("Not implemented".to_string())
}