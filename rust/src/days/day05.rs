use std::collections::VecDeque;
use std::fs::File;
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };

use crate::util::collect_array;

type CrateRow = Vec<Option<char>>;
type CrateStack = Vec<char>;

struct CrateStacks {
    // rows: VecDeque<CrateRow>,
    stacks: Vec<CrateStack>,
    crane_moves: Box<dyn Iterator<Item = String>>,
}

struct CraneMove {
    num: usize,
    from: usize,
    to: usize,
}

impl CrateStacks {
    pub fn new(mut lines: Box<dyn Iterator<Item = String>>) -> Self {
        let crate_stacks = CrateStacks::parse_crate_stacks(&mut lines);
        CrateStacks { stacks: crate_stacks, crane_moves: lines }
    }

    fn parse_crate_stacks(lines: &mut dyn Iterator<Item = String>) -> Vec<CrateStack> {
        let mut crate_stack_rows: VecDeque<CrateRow> = VecDeque::new();
        for row in lines {
            if row.is_empty() { break; }
            let crate_row = row
                .chars()
                .collect::<CrateStack>();
            let crate_names = crate_row
                .chunks(4)
                .map(|name| {
                    name
                        .iter()
                        .find(|c| { c.is_alphabetic() })
                        .map(|c| { c.to_owned() })
                });
            crate_stack_rows.push_front(crate_names.collect())
        }
        crate_stack_rows.pop_front();


       Self::rows_to_stacks(crate_stack_rows)
    }

    fn rows_to_stacks(rows: VecDeque<CrateRow>) -> Vec<CrateStack> {
        assert!(!rows.is_empty());

        (0..rows[0].len())
            .map(|stack_index| {
                let mut stack = Vec::new();
                rows.iter()
                    .for_each(|row| {
                        if let Some(crate_name) = row[stack_index] {
                            stack.push(crate_name);
                        }
                    });
                stack
            })
            .collect()
    }

    pub fn exec_all_crane_9000(self) -> String {
        let mut new_crate_stacks = self.stacks;
        for line in self.crane_moves {
            let crane_move = CrateStacks::parse_crane_move(&line);
            new_crate_stacks = CrateStacks::exec_crane_9000(new_crate_stacks, crane_move);
        }

        // FIXME: Possibly get the answer in a separate function?
        let mut answer = String::new();

        // Kind of messy since this mutates the final crate_stack...
        new_crate_stacks
            .iter_mut()
            .for_each(|stack| {
                answer.push(stack.pop().unwrap())
            });


        answer
    }

    pub fn exec_all_crane_9001(self) -> String {
        let mut new_crate_stacks = self.stacks;
        for line in self.crane_moves {
            let crane_move = CrateStacks::parse_crane_move(&line);
            new_crate_stacks = CrateStacks::exec_crane_9001(new_crate_stacks, crane_move);
        }

        // FIXME: Possibly get the answer in a separate function?
        let mut answer = String::new();

        // Kind of messy since this mutates the final crate_stack...
        new_crate_stacks
            .iter_mut()
            .for_each(|stack| {
                answer.push(stack.pop().unwrap())
            });


        answer
    }

    fn exec_crane_9000(crate_rows: Vec<CrateStack>, crane_move: CraneMove) -> Vec<CrateStack> {
        let mut new_crate_stacks = crate_rows;
        for _ in 0..crane_move.num {
            new_crate_stacks = CrateStacks::move_one(new_crate_stacks, crane_move.from-1, crane_move.to-1);
        }

        new_crate_stacks
    }

    fn move_one(crate_rows: Vec<CrateStack>, from: usize, to: usize) ->  Vec<CrateStack> {
        let mut new_crate_stacks = crate_rows;
        
        let crate_to_move = new_crate_stacks[from].pop().unwrap();
        new_crate_stacks[to].push(crate_to_move);
        
        new_crate_stacks
    }

    fn exec_crane_9001(crate_rows: Vec<CrateStack>, crane_move: CraneMove) -> Vec<CrateStack> {
        let mut new_crate_stacks = crate_rows;

        let mut moved_crates = Vec::new();

        for _ in 0..crane_move.num {
            let crate_to_move = new_crate_stacks[crane_move.from-1].pop().unwrap();
            moved_crates.push(crate_to_move);
        }

        for _ in 0..crane_move.num {
            let crate_to_move = moved_crates.pop().unwrap();
            new_crate_stacks[crane_move.to-1].push(crate_to_move);
        }

        new_crate_stacks
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
    let answer = crate_stacks.exec_all_crane_9000();
    Ok(answer)
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let lines = reader
        .lines()
        .flatten();
    
    let crate_stacks = CrateStacks::new(Box::new(lines));
    let answer = crate_stacks.exec_all_crane_9001();
    Ok(answer)
}