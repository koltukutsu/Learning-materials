use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    let mut count: u8 = 0;
    println!("Guess the number ranging from 1 to 100...");
    let secret_number: u32 = rand::thread_rng().gen_range(1..=100);
    println!("Plase input your guess:");

    loop {
        let mut guess = String::new();

        io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        println!("You guesses: {guess}");
        if count >= 5 {
            println!("Secret number is: {secret_number}");
        } else {
            count += 1;
        }
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Wuuw, it's quite cold man :D"),
            Ordering::Greater => println!("Oopps, it's hot :D"),
            Ordering::Equal => {
                println!("Hey, you got the same number with the computer. You won!!!");
                break;
            },
        }
    }
    
}
