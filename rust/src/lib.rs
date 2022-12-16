mod day01;

use std::path::PathBuf;
use std::fs::{self, DirEntry};
use std::io::Result;

use day01::day01_pt1;

const INPUT_DIR: &str = "../inputs";

pub type Days = Vec<Vec<&'static dyn Fn(&PathBuf) -> Result<u64>>>;

pub fn get_days() -> Days { vec![vec![&day01_pt1]] }

pub fn get_input_files() -> Result<Vec<DirEntry>> {
  let mut directory = fs::read_dir(INPUT_DIR)?
        .collect::<Result<Vec<_>>>()?;
  
  directory.sort_unstable_by_key(|dir| dir.path());

  Ok(directory)
}