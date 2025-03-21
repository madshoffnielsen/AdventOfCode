import re
from functools import lru_cache

def read_input(file_path):
    """Reads and parses the input file."""
    with open(file_path, "r") as f:
        return f.read().strip()

def parse_blueprints(input_data):
    """Parses the input data into a list of blueprints."""
    blueprints = []
    for line in input_data.split("\n"):
        nums = list(map(int, re.findall(r"\d+", line)))
        blueprint = {
            "id": nums[0],
            "ore": nums[1],  # Ore robot cost
            "clay": nums[2],  # Clay robot cost
            "obsidian": (nums[3], nums[4]),  # Obsidian robot cost (ore, clay)
            "geode": (nums[5], nums[6])  # Geode robot cost (ore, obsidian)
        }
        blueprints.append(blueprint)
    return blueprints

def max_geodes(blueprint, time_limit):
    """Calculates the maximum geodes that can be collected within the time limit."""
    max_ore_cost = max(blueprint["ore"], blueprint["clay"], blueprint["obsidian"][0], blueprint["geode"][0])

    @lru_cache(None)
    def dfs(time, ore, clay, obsidian, geodes, ore_r, clay_r, obsidian_r, geode_r):
        # Base case: if time runs out, return geodes
        if time == 0:
            return geodes

        best = geodes  # Track best geode count

        # Build geode robot if possible
        if ore >= blueprint["geode"][0] and obsidian >= blueprint["geode"][1]:
            return dfs(
                time - 1,
                ore - blueprint["geode"][0] + ore_r,
                clay + clay_r,
                obsidian - blueprint["geode"][1] + obsidian_r,
                geodes + geode_r,
                ore_r, clay_r, obsidian_r, geode_r + 1
            )

        # Build obsidian robot if possible
        if ore >= blueprint["obsidian"][0] and clay >= blueprint["obsidian"][1] and obsidian_r < blueprint["geode"][1]:
            best = max(best, dfs(
                time - 1,
                ore - blueprint["obsidian"][0] + ore_r,
                clay - blueprint["obsidian"][1] + clay_r,
                obsidian + obsidian_r,
                geodes + geode_r,
                ore_r, clay_r, obsidian_r + 1, geode_r
            ))

        # Build clay robot if possible
        if ore >= blueprint["clay"] and clay_r < blueprint["obsidian"][1]:
            best = max(best, dfs(
                time - 1,
                ore - blueprint["clay"] + ore_r,
                clay + clay_r,
                obsidian + obsidian_r,
                geodes + geode_r,
                ore_r, clay_r + 1, obsidian_r, geode_r
            ))

        # Build ore robot if possible
        if ore >= blueprint["ore"] and ore_r < max_ore_cost:
            best = max(best, dfs(
                time - 1,
                ore - blueprint["ore"] + ore_r,
                clay + clay_r,
                obsidian + obsidian_r,
                geodes + geode_r,
                ore_r + 1, clay_r, obsidian_r, geode_r
            ))

        # Do nothing (let time pass)
        best = max(best, dfs(
            time - 1,
            ore + ore_r,
            clay + clay_r,
            obsidian + obsidian_r,
            geodes + geode_r,
            ore_r, clay_r, obsidian_r, geode_r
        ))

        return best

    return dfs(time_limit, 0, 0, 0, 0, 1, 0, 0, 0)  # Start with 1 ore robot

def part1(blueprints):
    """Solves Part 1 by calculating the sum of blueprint quality levels."""
    return sum(bp["id"] * max_geodes(bp, 24) for bp in blueprints)

def part2(blueprints):
    """Solves Part 2 by calculating the product of max geodes for the first 3 blueprints."""
    result = 1
    for bp in blueprints[:3]:
        result *= max_geodes(bp, 32)
    return result

def main():
    print("\n--- Day 19: Not Enough Minerals ---")
    file_path = "2022/input/day19.txt"
    input_data = read_input(file_path)
    blueprints = parse_blueprints(input_data)

    # Part 1
    result1 = part1(blueprints)
    print(f"Part 1: {result1}")

    # Part 2
    result2 = part2(blueprints)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()