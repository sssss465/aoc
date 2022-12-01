use std::fs;

pub fn main() {
    let contents = fs::read_to_string("1").unwrap();
    let mut sorted: Vec<i32> = contents
        .split("\n\n")
        .map(|set| set.lines().flat_map(|line| line.parse::<i32>()).sum())
        .collect::<Vec<i32>>();
    sorted.sort();
    println!("silver: {}", sorted.last().unwrap());
    println!("gold: {}", sorted.iter().rev().take(3).sum::<i32>());
}
