use std::collections::HashMap;

fn points(l: u8, r: u8) -> u8 {
    if l == r {
        3 + r
    } else if l == 1 + (r + 1) % 3 {
        6 + r
    } else {
        r
    }
}

pub fn main() {
    let contents = include_str!("../2");
    let lines = contents
        .lines()
        .map(|set| set.split(' ').collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let nxt = HashMap::from([("A", " CAB"), ("B", " ABC"), ("C", " BCA")]);
    let score = HashMap::from([("A", 1), ("B", 2), ("C", 3), ("X", 1), ("Y", 2), ("Z", 3)]);

    let mut silver: i32 = 0;
    let mut gold: i32 = 0;
    for v in lines {
        let (l, r) = (v[0], v[1]);
        silver += points(score[l], score[r]) as i32;
        gold += points(
            score[l],
            score[nxt[l]
                .chars()
                .nth(score[r] as usize)
                .unwrap()
                .to_string()
                .as_str()],
        ) as i32;
    }

    println!("silver: {}", silver);
    println!("gold: {}", gold);
}
