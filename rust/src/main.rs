fn problem1_v2() -> u32 {
    (1..1000).filter(|num| num % 3 == 0 || num % 5 == 0).sum()
}

fn problem1() -> u32 {
    let mut sum = 0;
    for num in 1..1000 {
        if num % 3 == 0 || num % 5 == 0 {
            sum += num;
        }
    }
    sum
}
fn main() {
    println!("{:?}", problem1());
    println!("{:?}", problem1_v2());
}
