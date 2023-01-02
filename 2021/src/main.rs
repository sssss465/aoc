fn main() {
    println!("Hello, world!");
    let mut x = 5;
    let mut s = String::from("hello");
    println!("The value of x is: {}", x);
    //test(x, &s);
    x += 1;
    println!("The value of x is: {}", x);
    s.push_str(" world");
    println!("The value of s is: {}", s);
}

fn test(parm: i32, s: &String) -> Vec<i32> {
    let x = 5;
    let y = {
        let x = 3;
        x + 1
    };
    let v = vec![1, 2, 3];
    v
}
