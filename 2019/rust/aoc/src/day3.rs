use std::collections::HashMap;

pub fn run(lines: &Vec<String>) {
    let wire1 = parse(&lines[0]);
    let wire2 = parse(&lines[1]);

    let (r1, r2) = wire1
        .keys()
        .filter(|p| wire2.contains_key(p))
        .map(|p| {
            let (x, y) = p;
            (x.abs() + y.abs(), wire1[p] + wire2[p])
        })
        .fold((i32::MAX, i32::MAX), |(a1, a2), (i1, i2)| {
            (a1.min(i1), a2.min(i2))
        });

    println!("part 1: {}", r1);
    println!("part 2: {}", r2);
}

fn parse(str: &String) -> HashMap<(i32, i32), i32> {
    let mut points = HashMap::new();
    let mut x = 0;
    let mut y = 0;
    let mut n = 0;

    for s in str.split(',') {
        let (l, r) = s.split_at(1);
        let len = r.parse::<i32>().unwrap();
        let (dx, dy) = match l {
            "R" => (1, 0),
            "L" => (-1, 0),
            "U" => (0, 1),
            "D" => (0, -1),
            _ => unreachable!(),
        };
        for _ in 0..len {
            x += dx;
            y += dy;
            n += 1;
            points.entry((x, y)).or_insert(n);
        }
    }
    points
}
