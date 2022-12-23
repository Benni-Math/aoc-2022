use std::fs::File;
use std::path::PathBuf;
use std::io::{ BufReader, BufRead };

use crate::util::collect_array;

// Gonna try manually scoring the games...
fn score_game_1(player1: char, player2: char) -> u64 {
    match (player1, player2) {
        ('A', 'X') => 4, // Rock, Rock
        ('A', 'Y') => 8, // Rock, Paper
        ('A', 'Z') => 3, // Rock, Scissors
        ('B', 'X') => 1, // Paper, Rock
        ('B', 'Y') => 5, // Paper, Paper
        ('B', 'Z') => 9, // Paper, Scissors
        ('C', 'X') => 7, // Scissors, Rock
        ('C', 'Y') => 2, // Scissors, Paper
        ('C', 'Z') => 6, // Scissors, Scissors
        _ => panic!(), // This should never happen...
    }
}

pub fn pt1(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(0, |sum, game| {
            let [player1, _, player2] = collect_array(game.chars());
            sum + score_game_1(player1, player2)
        });

    Ok(format!("{}", answer))
}


fn score_game_2(player1: char, player2: char) -> u64 {
    match (player1, player2) {
        ('A', 'X') => 3, // Rock, Scissors
        ('A', 'Y') => 4, // Rock, Rock
        ('A', 'Z') => 8, // Rock, Paper
        ('B', 'X') => 1, // Paper, Rock
        ('B', 'Y') => 5, // Paper, Paper
        ('B', 'Z') => 9, // Paper, Scissors
        ('C', 'X') => 2, // Scissors, Paper
        ('C', 'Y') => 6, // Scissors, Scissors
        ('C', 'Z') => 7, // Scissors, Rock
        _ => panic!(), // This should never happen...
    }
}

pub fn pt2(filename: &PathBuf) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let answer = reader
        .lines()
        .flatten()
        .fold(0, |sum, game| {
            let [player1, _, player2] = collect_array(game.chars());
            sum + score_game_2(player1, player2)
        });

    Ok(format!("{}", answer))
}