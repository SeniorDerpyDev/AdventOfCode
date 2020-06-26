use std::fs::File;
use std::io::{BufRead, BufReader};

mod day1;
mod day3;

fn read_input(path: String) -> std::io::Result<Vec<String>> {
    let file = File::open(path)?;
    let lines = BufReader::new(file).lines();
    Ok(lines.map(|l| l.unwrap()).collect::<Vec<String>>())
}

fn main() {
    let arg = std::env::args().nth(1).expect("you must give me a day");
    let path = std::env::args()
        .nth(2)
        .expect("you must give me a file path");
    let day = arg.parse::<i32>().expect("that's not a number");
    let lines = read_input(path).expect("there's something wrong with that path");

    match day {
        1 => day1::run(&lines),
        3 => day3::run(&lines),
        _ => eprintln!("unknown day!"),
    }
}
