use std::collections::HashSet;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut set = HashSet::new();
    let mut v = Vec::new();

    for line in stdin.lock().lines() {
        let a = line.unwrap().parse::<i32>().unwrap();
        v.push(a);
    }

    let sl = &v[..];
    for (i, a) in sl.iter().enumerate() {
        if set.contains(&(2020 - a)) {
            println!("part 1: {}", (2020 - a) * a);
        }

        for b in &v[i + 1..] {
            if set.contains(&(2020 - (a + b))) {
                println!("part 2: {}", (2020 - (a + b)) * a * b);
            }
        }
        set.insert(a);
    }
}
