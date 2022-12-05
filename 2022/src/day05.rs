use regex::Regex;
use std::collections::HashMap;

pub fn main() {
    let input = include_str!("../5");
    let mut mp: HashMap<usize, Vec<&str>> = HashMap::new();
    let mut mp2: HashMap<usize, Vec<&str>> = HashMap::new();
    input
        .lines()
        .take(8)
        .flat_map(|s| {
            let re = Regex::new(r"(?:\[([A-Z])\]|\s(\s{3}))").unwrap();
            let c = re.captures_iter(s);
            let vv = c
                .enumerate()
                .filter_map(|(i, m)| m.get(1).map(|m| (i + 1, m.as_str())))
                .filter(|(_, v)| !v.contains(' '))
                .collect::<Vec<_>>();
            // dbg!(&vv);
            vv
        })
        .for_each(|(i, v)| {
            //dbg!("pushing", i, v);
            mp.entry(i).or_insert(vec![]).push(v);
            mp2.entry(i).or_insert(vec![]).push(v);
        });
    mp.iter_mut().for_each(|(_i, v)| v.reverse());
    mp2.iter_mut().for_each(|(_i, v)| v.reverse());
    input.lines().skip(10).for_each(|s| {
        let re = Regex::new(r" (\d+)").unwrap();
        let v = re
            .find_iter(s)
            .map(|m| m.as_str().trim().parse::<usize>().unwrap())
            .collect::<Vec<_>>();
        let (amt, from, to) = (v[0], v[1], v[2]);
        let v = mp.get_mut(&from).unwrap();
        let v2 = mp2.get_mut(&from).unwrap();
        let mut f = v.split_off(v.len() - amt);
        let f2 = v2.split_off(v2.len() - amt);
        f.reverse();
        {
            mp.get_mut(&to).unwrap().extend(f);
            mp2.get_mut(&to).unwrap().extend(f2);
        }
    });
    let res = [mp, mp2]
        .iter()
        .map(|mp| {
            (1..mp.len() + 1).fold("".to_string(), |mut acc, i| {
                acc.push_str(mp.get(&i).unwrap().last().unwrap());
                acc
            })
        })
        .collect::<Vec<_>>();
    println!("silver: {}\ngold: {}", res[0], res[1]);
}
