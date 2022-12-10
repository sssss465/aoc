pub fn main() {
    let lines: Vec<&str> = include_str!("../10").lines().collect();
    let (mut x, mut cycle, mut silver, mut screen) = (1, 0, 0, vec![' '; 240]);

    for l in lines {
        let (cmd, v) = if l == "noop" {
            ("noop", 0)
        } else {
            let parts: Vec<&str> = l.split(' ').collect();
            (parts[0], parts[1].parse::<i32>().unwrap())
        };
        for _ in 0..(if cmd == "addx" { 2 } else { 1 }) {
            if (cycle + 1) % 40 == 20 {
                silver += (cycle + 1) * x;
            }
            if cycle % 40 == (x - 1) || cycle % 40 == x || cycle % 40 == (x + 1) {
                screen[cycle as usize] = '#';
            }
            cycle += 1;
        }
        x += v;
    }

    println!("silver : {}", silver);
    println!("gold");
    for i in (0..240).step_by(40) {
        for j in i..i + 40 {
            print!("{}", screen[j]);
        }
        println!();
    }
}
