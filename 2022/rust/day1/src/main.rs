use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::cmp::Reverse;

fn main() -> io::Result<()> {
    let file_path = "input.txt";

    let file = File::open(file_path)?;
    let reader = BufReader::new(file);

    let mut temp = 0;
    let mut r_vec: Vec<i32> = Vec::new();

    for line in reader.lines() {
        if let Ok(line) = line {
            if line.is_empty() {
                if temp > 0 && (r_vec.len() < 3 || temp > r_vec[r_vec.len() - 1]) {
                    r_vec.push(temp);
                    r_vec.sort_by_key(|&x| Reverse(x));
                    if r_vec.len() > 3 {
                        r_vec.truncate(3);
                    }
                }
                temp = 0;
            } else {
                let val: i32 = line.parse().expect("Error converting to integer");
                temp += val;
            }
        }
    }

    println!("The top three are:");
    println!("{:?}", rslice);

    let sum: i32 = rslice.iter().sum();
    println!("Sum of top three: {}", sum);

    Ok(())
}
