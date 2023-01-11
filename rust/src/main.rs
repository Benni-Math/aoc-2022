use rayon::prelude::*;

use aoc_2022::{ ALL_DAYS, get_input_files };

fn main() -> std::io::Result<()> {
    let input_files = get_input_files()?;

    // Could probably make this multithreaded...
    let output = ALL_DAYS
        .par_iter()
        .zip(input_files)
        .enumerate()
        .map(|(day, (solutions, filename))| {
            let mut soln = format!("Day {}:", day+1);
            if let Ok(answer_pt1) = solutions.0(&filename.path()) {
                soln.push_str(&format!("\n  Part 1: {}", answer_pt1));
            }
            if let Ok(answer_pt2) = solutions.1(&filename.path()) {
                soln.push_str(&format!("\n  Part 2: {}", answer_pt2));
            }
            soln.push_str("\n\n");

            soln
        })
        .reduce(String::new, |mut acc, out| {
            acc.push_str(&out);
            acc
        });
    print!("{}", output);
    Ok(())
}
