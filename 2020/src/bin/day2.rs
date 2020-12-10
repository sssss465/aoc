use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut v = Vec::new();
    for line in stdin.lock().lines() {
        let l = line.unwrap();
        let a: Vec<&str> = l.split(" ").collect();
        v.push(a);
    }


}
