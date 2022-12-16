use aoc_2022::{ get_days, get_input_files };

fn main() -> std::io::Result<()> {
    let input_files = get_input_files()?;

    let days = get_days();

    // Could probably make this multithreaded...
    days.iter()
        .enumerate()
        .for_each(|(day, solutions)| {
            let filename = match input_files.get(day) {
                Some(dir_entry) => dir_entry.path(),
                None => panic!(),
            };
            solutions.iter()
                .enumerate()
                .for_each(|(part, soln_func)| {
                    if let Ok(answer) = soln_func(&filename) {
                        println!("Day {}, pt{}: {}", day+1, part+1, answer);
                    }
                })
        });

    Ok(())
}
