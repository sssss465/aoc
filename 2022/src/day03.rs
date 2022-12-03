use std::collections::HashSet;

pub fn main() {
    let input = include_str!("../3");

    let s: u32 = input
        .lines()
        .map(|line| {
            let a: HashSet<char> = HashSet::from_iter(line.chars().take(line.len() / 2));
            let b: HashSet<char> = HashSet::from_iter(line.chars().skip(line.len() / 2));
            a.intersection(&b).next().unwrap().to_owned()
        })
        .map(|c| {
            let p = c as u32;
            p % 32 + 26 * (p >> 5 & 1 ^ 1) // thanks sheks
        })
        .sum();

    let g: u32 = input
        .lines()
        .step_by(3)
        .zip(input.lines().skip(1).step_by(3))
        .zip(input.lines().skip(2).step_by(3))
        .map(|((a, b), c)| {
            let mut a: HashSet<char> = HashSet::from_iter(a.chars());
            let b: HashSet<char> = HashSet::from_iter(b.chars());
            let c: HashSet<char> = HashSet::from_iter(c.chars());
            a.retain(|x| b.contains(x) && c.contains(x));
            a.iter().next().unwrap().to_owned()
        })
        .map(|c| {
            let p = c as u32;
            p % 32 + 26 * (p >> 5 & 1 ^ 1) // thanks sheks
        })
        .sum();

    println!("silver: {}", s);
    println!("gold: {}", g);
}
