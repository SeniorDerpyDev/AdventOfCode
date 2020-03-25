pub fn run(lines: &Vec<String>) {
    let r = part1(lines);
    println!("part 1: {}", r);

    let r = part2(lines);
    println!("part 2: {}", r);
}

fn part1(lines: &Vec<String>) -> i32 {
    lines
        .iter()
        .map(|s| {
            let mass = s.parse::<i32>().unwrap();
            mass / 3 - 2
        })
        .sum()
}

fn part2(lines: &Vec<String>) -> i32 {
    lines
        .iter()
        .map(|s| {
            let mass = s.parse::<i32>().unwrap();
            calc_fuel(mass)
        })
        .sum()
}

fn calc_fuel(mass: i32) -> i32 {
    let fuel = mass / 3 - 2;
    if fuel <= 0 {
        0
    } else {
        fuel + calc_fuel(fuel)
    }
}
