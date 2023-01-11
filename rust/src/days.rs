mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;
mod day07;
mod day08;
mod day09;
mod day10;
mod day11;
mod day12;
mod day13;
mod day14;
mod day15;
mod day16;
mod day17;
mod day18;
mod day19;
mod day20;
mod day21;
mod day22;
mod day23;
mod day24;
mod day25;


use std::path::PathBuf;
use crate::Result;

pub type Part = &'static (dyn Fn(&PathBuf) -> Result<String> + Send + Sync);
pub type Day = (Part, Part);
pub type Days = [Day; 25];

pub const ALL_DAYS: Days = [
        (&day01::pt1, &day01::pt2),
        (&day02::pt1, &day02::pt2),
        (&day03::pt1, &day03::pt2),
        (&day04::pt1, &day04::pt2),
        (&day05::pt1, &day05::pt2),
        (&day06::pt1, &day06::pt2),
        (&day07::pt1, &day07::pt2),
        (&day08::pt1, &day08::pt2),
        (&day09::pt1, &day09::pt2),
        (&day10::pt1, &day10::pt2),
        (&day11::pt1, &day11::pt2),
        (&day12::pt1, &day12::pt2),
        (&day13::pt1, &day13::pt2),
        (&day14::pt1, &day14::pt2),
        (&day15::pt1, &day15::pt2),
        (&day16::pt1, &day16::pt2),
        (&day17::pt1, &day17::pt2),
        (&day18::pt1, &day18::pt2),
        (&day19::pt1, &day19::pt2),
        (&day20::pt1, &day20::pt2),
        (&day21::pt1, &day21::pt2),
        (&day22::pt1, &day22::pt2),
        (&day23::pt1, &day23::pt2),
        (&day24::pt1, &day24::pt2),
        (&day25::pt1, &day25::pt2),
];