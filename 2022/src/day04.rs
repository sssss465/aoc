use regex::Regex;
use std::cmp::{max, min};

pub fn main() {
    let input = include_str!("../4");
    let re = Regex::new(r"(\d+)-(\d+),(\d+)-(\d+)").unwrap();
    let r = input.lines().fold((0, 0), |(mut s, mut g), line| {
        let c = re.captures(line).unwrap();
        let mut p1 = (
            c[1].parse::<usize>().unwrap(),
            c[2].parse::<usize>().unwrap(),
        );
        let mut p2 = (
            c[3].parse::<usize>().unwrap(),
            c[4].parse::<usize>().unwrap(),
        );
        if p1.0 > p2.0 {
            std::mem::swap(&mut p1, &mut p2);
        }
        s += (p1.1 >= p2.1 || p1.0 == p2.0) as usize;
        g += (max(p1.0, p2.0) <= min(p1.1, p2.1)) as usize;
        (s, g)
    });
    println!("silver: {}\ngold: {}", r.0, r.1);
}
