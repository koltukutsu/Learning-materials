use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Guess the number ranging from 1 to 100...");
    let secret_number = rand::thread_rng().gen_range(1..=100);
    print!("Plase input your guess:\n> ");

    let mut guess = String::new();
    loop {
        io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

        let guess: u32 = guess.trim().parse().expect("Please type a number");
        println!("You guesses: {guess}");
        
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
