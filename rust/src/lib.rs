mod util;
mod days;

use std::fs::{self, DirEntry};
pub use std::io::Result;

pub use days::*;


const INPUT_DIR: &str = "../inputs";


pub fn get_input_files() -> Result<Vec<DirEntry>> {
    let mut directory = 
        fs::read_dir(INPUT_DIR)?
        .collect::<Result<Vec<_>>>()?;
    
    directory.sort_unstable_by_key(|dir| dir.path());

    Ok(directory)
}