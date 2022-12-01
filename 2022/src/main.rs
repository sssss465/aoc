mod day01;
fn main() {
    let args: Vec<String> = std::env::args().collect();
    let day: i32 = args
        .get(1)
        .or_else(|| panic!("Usage: <day>"))
        .and_then(|s| s.parse::<i32>().map_err(|e| panic!("{:?}", e)).ok())
        .unwrap_or_else(|| panic!("Use a number for the day"));

    match day {
        1 => day01::main(),
        _ => println!("Day {} not implemented", day),
    }
}
