use std::collections::VecDeque;

struct State {
    // [ore, clay, obsidian, geode]
    inventory: [u16; 4],
    // [ore_bots, clay_bots, obsidian_bots, geode_bots]
    bots: [u16; 4],
    // elapsed time in minutes
    elapsed: u16,
}

// each cost is [ore_amount, clay_amount, obsidian_amount, geode_amount]
// [ore_bot_costs, clay_bot_costs, obsidian_bot_costs, geode_bot_costs]
fn parse() -> Vec<[[u16; 4]; 4]> {
    let input = include_str!("../19");
    let mut blueprints = Vec::new();

    for line in input.lines() {
        let mut iter = line.split_ascii_whitespace();

        // ore bots cost ore
        let ore_bot_costs = [iter.nth(6).unwrap().parse().unwrap(), 0, 0, 0];
        // clay bots cost ore
        let clay_bot_costs = [iter.nth(5).unwrap().parse().unwrap(), 0, 0, 0];
        // obsidian bots cost ore and clay
        let obsidian_bot_costs = [
            iter.nth(5).unwrap().parse().unwrap(),
            iter.nth(2).unwrap().parse().unwrap(),
            0,
            0,
        ];
        // geode bots cost ore and obsidian
        let geode_bot_costs = [
            iter.nth(5).unwrap().parse().unwrap(),
            0,
            iter.nth(2).unwrap().parse().unwrap(),
            0,
        ];

        let blueprint = [
            ore_bot_costs,
            clay_bot_costs,
            obsidian_bot_costs,
            geode_bot_costs,
        ];
        blueprints.push(blueprint);
    }

    blueprints
}

fn max_geodes(blueprint: &[[u16; 4]; 4], max_time: u16) -> u16 {
    // calculate the maximum amount for every type of bot so that the creation of a new bot of any type is never bottlenecked
    // it doesn't make sense to build more bots than that maximum if the resources a bot type generates are
    // enough to cover that type (ore, clay, obsidian) cost for any possible bot (per question, you can only build 1 bot per turn)
    // for geode bots, there is no logical maximum amount
    // [ore, clay, obsidian, geode]
    let mut max_robots = [u16::MAX; 4];
    for i in 0..3 {
        max_robots[i] = blueprint.iter().map(|cost| cost[i]).max().unwrap();
    }
    let mut max_geodes = 0;
    let mut max_size: usize = 0;
    let mut q = VecDeque::new();
    q.push_back(State {
        inventory: [0, 0, 0, 0],
        bots: [1, 0, 0, 0],
        elapsed: 0,
    });

    while let Some(State {
        inventory,
        bots,
        elapsed,
    }) = q.pop_front()
    {
        // for every bot cost, run simulation
        for i in 0..blueprint.len() {
            // if we already have enough of this bot type, skip
            if bots[i] == max_robots[i] {
                continue;
            }

            let costs = &blueprint[i];

            // Find the limiting resource type for the costs.
            let wait_time = (0..3)
                .map(|idx| {
                    match costs[idx] {
                        // state has enough of current resource in inventory to cover that part of the target bot cost. 0 wait time
                        cost if cost <= inventory[idx] => 0,
                        // no target bot type made yet
                        // we can't build it (it takes more than max_time to build it).
                        _ if bots[idx] == 0 => max_time + 1,
                        _ => (costs[idx] - inventory[idx] + bots[idx] - 1) / bots[idx],
                    }
                })
                .max()
                .unwrap();

            // if that choice would cause the time limit be to exceeded, skip
            // the + 1 is so the built bot has the chance to do something, it merely being built is not enough
            let new_elapsed = elapsed + wait_time + 1;
            if new_elapsed >= max_time {
                continue;
            }

            // gather ores with previously available bots
            let mut new_inventory = [0; 4];
            for idx in 0..bots.len() {
                new_inventory[idx] = inventory[idx] + bots[idx] * (wait_time + 1) - costs[idx];
            }

            // increase bot type for the bot we just built
            let mut new_bots = bots.clone();
            new_bots[i] += 1;

            // extra optimization:
            // if we theoretically only built geode bots every turn, and we still don't beat the maximum, skip
            let remaining_time = max_time - new_elapsed;
            if ((remaining_time - 1) * remaining_time) / 2
                + new_inventory[3]
                + remaining_time * new_bots[3]
                < max_geodes
            {
                continue;
            }

            q.push_back(State {
                inventory: new_inventory,
                bots: new_bots,
                elapsed: new_elapsed,
            })
        }
        max_size = max_size.max(q.len());
        let geodes = inventory[3] + bots[3] * (max_time - elapsed);
        max_geodes = geodes.max(max_geodes);
    }
    // println!("Max size: {}", max_size);
    max_geodes
}

pub fn part_1() -> usize {
    let blueprints = parse();

    blueprints
        .iter()
        .map(|blueprint| max_geodes(blueprint, 24))
        .enumerate()
        .map(|(idx, geodes)| (idx + 1) * usize::from(geodes))
        .sum()
}

pub fn part_2() -> usize {
    let blueprints = parse();

    blueprints
        .iter()
        .take(3)
        .map(|blueprint| usize::from(max_geodes(blueprint, 32)))
        .product()
}

pub fn main() {
    println!("Part 1: {}", part_1());
    println!("Part 2: {}", part_2());
}
