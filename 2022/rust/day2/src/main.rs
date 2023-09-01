use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::collections::HashMap;


fn main() -> io::Result<()> {
    let file_path = "input.txt";

    let infiile = File::open(file_path)?;
    let reader = BufReader::new(infiile);

    let scores_map = {
        let mut m = HashMap::new();
        m.insert("X", 1);
        m.insert("Y", 2);
        m.insert("Z", 3);
        m
    };

    let mut outcome = HashMap::new();
    // Add some key-value pairs to the hash map.
    outcome.insert("X", HashMap::new());
    outcome.get_mut("X").unwrap().insert("A", "draw");
    outcome.get_mut("X").unwrap().insert("B", "lose");
    outcome.get_mut("X").unwrap().insert("C", "win");
  
    outcome.insert("Y", HashMap::new());
    outcome.get_mut("Y").unwrap().insert("A", "win");
    outcome.get_mut("Y").unwrap().insert("B", "draw");
    outcome.get_mut("Y").unwrap().insert("C", "lose");

    outcome.insert("Z", HashMap::new());
    outcome.get_mut("Z").unwrap().insert("A", "lose");
    outcome.get_mut("Z").unwrap().insert("B", "win");
    outcome.get_mut("Z").unwrap().insert("C", "draw");
  
    let mut score = 0;
    for line in reader.lines() {
        if let Ok(line) = line {
            let mut weapons = line.split_whitespace();
            let theres = weapons.next().unwrap();
            let mine = weapons.next().unwrap();

            // println!("Mine is {} and theres is {}", mine, theres);

            if let Some(inner_map) = outcome.get(mine) {
                if let Some(result) = inner_map.get(theres) {
                    if result == &"draw" {
                        score += 3;
                    } else if result == &"win" {
                        score += 6;
                    }
                }
            }

            score = score + scores_map[mine];
        }
    }

    println!("The Score is {}", score);
    Ok(())

}
