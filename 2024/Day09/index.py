def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def parse_input(string):
    file_system = []
    file_sizes = {}
    empty_space = {}
    file = True
    id = 0
    for char in string:
        if file:
            for i in range(int(char)):
                file_system.append(id)
            
            file_sizes[id] = int(char)
            id += 1
            file = False
        else:
            empty_space[len(file_system)] = int(char)
            for i in range(int(char)):
                file_system.append(".")
            file = True

    return file_system, file_sizes, empty_space

def defrag_file_system(file_system):
    defragged = []
    last_id = len(file_system) - 1
    for i in range(len(file_system)):
        if i > last_id:
            break
        if file_system[i] == ".":
            while file_system[last_id] == ".":
                last_id -= 1
            defragged.append(file_system[last_id])
            last_id -= 1
        else:
            defragged.append(file_system[i])
    
    return defragged

def defrag_file_system_whole_file(file_system, file_sizes, empty_space):
    # Create a copy to avoid modifying original
    fs = file_system.copy()
    
    # Get list of file IDs sorted in descending order
    file_ids = sorted([fid for fid in file_sizes.keys()], reverse=True)
    
    for file_id in file_ids:
        # Find current position of file
        start_pos = -1
        for i, val in enumerate(fs):
            if val == file_id:
                start_pos = i
                break
        
        if start_pos == -1:
            continue
            
        size = file_sizes[file_id]
        
        # Find leftmost valid free space
        best_pos = -1
        for pos in sorted(empty_space.keys()):
            if pos >= start_pos:  # Don't move file right
                continue
            if empty_space[pos] >= size:  # Space must fit file
                best_pos = pos
                break
        
        # Move file if valid position found
        if best_pos != -1:
            # Move file
            for i in range(size):
                fs[best_pos + i] = file_id
                fs[start_pos + i] = "."
            
            # Update empty spaces
            new_space_pos = start_pos
            new_space_size = size
            empty_space[new_space_pos] = new_space_size
            
            if best_pos in empty_space:
                empty_space[best_pos + size] = empty_space[best_pos] - size
                del empty_space[best_pos]
    
    return fs

def calculate_checksum(file_system):
    checksum = 0
    for i in range(len(file_system)):
        if file_system[i] != ".":
            checksum += file_system[i] * i
    
    return checksum

def defrag(string, whole_file=False):
    file_system, file_sizes, empty_space = parse_input(string)
    
    if whole_file:
        defrag_file = defrag_file_system_whole_file(file_system, file_sizes, empty_space)
    else:
        defrag_file = defrag_file_system(file_system)
    
    checksum = calculate_checksum(defrag_file)

    return checksum

def main():
    string = read_input("2024/Day09/input.txt")
    print(f"Part 1: {defrag(string)}")
    print(f"Part 2: {defrag(string, True)}")

if __name__ == "__main__":
    main()