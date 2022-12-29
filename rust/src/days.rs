mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;

use std::path::PathBuf;
use crate::Result;



pub type Days = Vec<Vec<&'static dyn Fn(&PathBuf) -> Result<String>>>;

pub fn get_days() -> Days { 
    vec![
        vec![&day01::pt1, &day01::pt2],
        vec![&day02::pt1, &day02::pt2],
        vec![&day03::pt1, &day03::pt2],
        vec![&day04::pt1, &day04::pt2],
        vec![&day05::pt1, &day05::pt2],
        vec![&day06::pt1, &day06::pt2],
    ] 
}