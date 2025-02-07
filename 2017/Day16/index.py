def read_input(file_path):
    with open(file_path) as f:
        return f.read().strip().split(',')

def dance_move(programs, move):
    programs = list(programs)
    if move[0] == 's':
        x = int(move[1:])
        programs = programs[-x:] + programs[:-x]
    elif move[0] == 'x':
        a, b = map(int, move[1:].split('/'))
        programs[a], programs[b] = programs[b], programs[a]
    else:  # move[0] == 'p'
        a, b = move[1:].split('/')
        i, j = programs.index(a), programs.index(b)
        programs[i], programs[j] = programs[j], programs[i]
    return ''.join(programs)

def dance(moves, programs='abcdefghijklmnop', times=1):
    seen = [programs]
    current = programs
    
    # Find cycle
    for i in range(times):
        for move in moves:
            current = dance_move(current, move)
        
        if current in seen:
            cycle_length = len(seen)
            return seen[times % cycle_length]
        seen.append(current)
    
    return current

def main():
    moves = read_input("2017/Day16/input.txt")
    print(f"Part 1: {dance(moves)}")
    print(f"Part 2: {dance(moves, times=1_000_000_000)}")

if __name__ == "__main__":
    main()