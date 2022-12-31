use std::collections::HashSet;
use std::path::PathBuf;

fn test_marker(slice: &[u8]) -> bool {
    let mut uniq = HashSet::new();
    slice.iter().all(move |x| uniq.insert(x))
}

pub fn pt1(filename: &PathBuf) -> std::io::Result<String> {
    let file = std::fs::read(filename)?;

    let marker_search = &file[..]
        .windows(4)
        .enumerate()
        .find(|(_, marker)| {
            test_marker(marker)
        });

    if let Some((answer, _)) = marker_search
        {
            return Ok(format!("{}", answer+4));
        }

    Ok("Could not find marker :(".to_string())
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = std::fs::read(filename)?;

    let marker_search = &file[..]
        .windows(14)
        .enumerate()
        .find(|(_, marker)| {
            test_marker(marker)
        });

    if let Some((answer, _)) = marker_search
        {
            return Ok(format!("{}", answer+14));
        }

    Ok("Could not find marker :(".to_string())
}