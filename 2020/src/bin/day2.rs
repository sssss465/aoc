use std::fs::File;
use std::io::BufReader;
use std::{collections::HashMap, io::BufRead};

fn main() {
    let reader = BufReader::new(File::open("inputs/2").unwrap());
    let mut v = Vec::new();
    for line in reader.lines() {
        let l = line.unwrap();
        let a: Vec<String> = l.split(" ").map(String::from).collect();
        v.push(a);
    }
    let (mut silver, mut gold) = (0, 0);
    for line in v {
        let res: Vec<i32> = line[0]
            .split("-")
            .map(|n| n.parse::<i32>().unwrap())
            .collect();
        let small = res[0];
        let big = res[1];
        let occ = line[1].chars().nth(0).unwrap();
        let mut map = HashMap::new();
        for c in line[2].chars().into_iter() {
            *map.entry(c).or_insert(0) += 1;
        }
        if map.contains_key(&occ) && map[&occ] >= small && map[&occ] <= big {
            silver += 1;
        }
        let pos1 = line[2].chars().nth((small - 1) as usize).unwrap();
        let pos2 = line[2].chars().nth((big - 1) as usize).unwrap();
        if pos1 != pos2 && (pos1 == occ || pos2 == occ) {
            gold += 1;
        }
    }

    println!("silver {}", silver);
    println!("gold {}", gold);
}
