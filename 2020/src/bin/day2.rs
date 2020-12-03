use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut v = Vec::new();
    for line in stdin.lock().lines() {
        let a: Vec<&str> = line.unwrap().split(" ");
        v.push(a);
    }
}
