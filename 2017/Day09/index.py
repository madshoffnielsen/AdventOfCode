def read_input(file_path):
    with open(file_path) as f:
        return f.read().strip()

def process_stream(stream):
    depth = 0
    total_score = 0
    garbage_count = 0
    in_garbage = False
    skip_next = False
    
    for char in stream:
        if skip_next:
            skip_next = False
            continue
            
        if char == '!':
            skip_next = True
            continue
            
        if in_garbage:
            if char == '>':
                in_garbage = False
            else:
                garbage_count += 1
            continue
            
        if char == '<':
            in_garbage = True
        elif char == '{':
            depth += 1
        elif char == '}':
            total_score += depth
            depth -= 1
            
    return total_score, garbage_count

def main():
    stream = read_input("2017/Day09/input.txt")
    score, garbage = process_stream(stream)
    print(f"Part 1: {score}")
    print(f"Part 2: {garbage}")

if __name__ == "__main__":
    main()