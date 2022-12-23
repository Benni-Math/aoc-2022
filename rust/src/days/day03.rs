use std::fs::File;
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };

use std::collections::HashSet;

fn compartment_comparison(comp1: &str, comp2: &str) -> char {
    let mut items = HashSet::new();
    for c in comp1.chars() {
        items.insert(c);
    }

    for c in comp2.chars() {
        if items.contains(&c) {
            return c;
        }
    }

    panic!("Failed to find shared item:\n\t{}\n\t{}", comp1, comp2)
}

fn get_priority(c: char) -> u64 {
    let ord = c as u32;
    if ord > 96 && ord < 123 { u64::from(ord) - 96 } 
    else if ord > 64 && ord < 91 { u64::from(ord) - 64 + 26 } 
    else { panic!("Failed to find priority: {}", c) }
}

pub fn pt1(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(0, |sum, line| {
            let halfway = line.len()/2;
            let shared_item = compartment_comparison(
                &line[..halfway],
                &line[halfway..],
            );

            sum + get_priority(shared_item)
        });

    Ok(format!("{}", answer))
}

fn group_comparison(elf1: &str, elf2: &str, elf3: &str) -> char {
    let mut elf1_items = HashSet::new();
    for c in elf1.chars() {
        elf1_items.insert(c);
    }

    let mut elf_pair_intersection = HashSet::new();
    for c in elf2.chars() {
        if elf1_items.contains(&c) {
            elf_pair_intersection.insert(c);
        }
    }

    for c in elf3.chars() {
        if elf_pair_intersection.contains(&c) {
            return c;
        }
    }

    panic!("Failed to find shared item:\n\t{}\n\t{}\n\t{}", elf1, elf2, elf3)
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .collect::<Vec<_>>()
        .chunks(3)
        .fold(0, |sum, group| {
            let [elf1, elf2, elf3] = group 
                else { panic!("Malformed elf group: {:?}", group) };
            let shared_item = group_comparison(elf1.as_ref(), elf2.as_ref(), elf3.as_ref());

            sum + get_priority(shared_item)
        });

    Ok(format!("{}", answer))
}