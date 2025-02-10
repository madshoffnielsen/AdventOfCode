def read_input(file_path):
    with open(file_path) as f:
        return [int(line.strip()) for line in f]

def count_differences(adapters):
    # Add charging outlet (0) and device adapter (max + 3)
    adapters = [0] + sorted(adapters) + [max(adapters) + 3]
    differences = {1: 0, 2: 0, 3: 0}
    
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i-1]
        differences[diff] += 1
    
    return differences[1] * differences[3]

def count_arrangements(adapters):
    # Add charging outlet and device adapter
    adapters = [0] + sorted(adapters) + [max(adapters) + 3]
    dp = {adapters[-1]: 1}  # Base case: one way to reach end
    
    for i in range(len(adapters)-2, -1, -1):
        current = adapters[i]
        dp[current] = 0
        
        # Check next possible adapters (1-3 jolts higher)
        for j in range(i+1, len(adapters)):
            if adapters[j] - current <= 3:
                dp[current] += dp[adapters[j]]
            else:
                break
    
    return dp[0]

def part1(adapters):
    return count_differences(adapters)

def part2(adapters):
    return count_arrangements(adapters)

def main():
    adapters = read_input("2020/Day10/input.txt")
    print(f"Part 1: {part1(adapters)}")
    print(f"Part 2: {part2(adapters)}")

if __name__ == "__main__":
    main()