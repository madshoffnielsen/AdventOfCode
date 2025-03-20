def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def process_filesystem(lines):
    total_score = 0
    total_score_part2 = float('inf')

    folder_size = {}
    filesystem = []

    for line in lines:
        args = line.strip().split(' ')

        # Change directory
        if args[0] == '$' and args[1] == 'cd':
            if args[2] == '..':
                filesystem.pop()
            else:
                if args[2] == '/':
                    filesystem.append('root')
                else:
                    filesystem.append(args[2])

        # Count file size
        if args[0].isdigit():
            depth = len(filesystem)

            for i in range(depth):
                depth_path = filesystem[:i+1]
                string_path = '/'.join(depth_path)

                if string_path in folder_size:
                    folder_size[string_path] += int(args[0])
                else:
                    folder_size[string_path] = int(args[0])

    total_score = sum(size for size in folder_size.values() if size <= 100000)

    disk_space = 70000000
    update_space = 30000000
    used_space = folder_size['root']

    free_space = disk_space - used_space
    needed_space = update_space - free_space

    for size in folder_size.values():
        if size >= needed_space and size < total_score_part2:
            total_score_part2 = size

    return total_score, total_score_part2

def main():
    print("\n--- Day 7: No Space Left On Device ---")
    lines = read_input('2022/input/day07.txt')
    total_score, total_score_part2 = process_filesystem(lines)

    print(f"Part 1: {total_score}")
    print(f"Part 2: {total_score_part2}")

if __name__ == "__main__":
    main()