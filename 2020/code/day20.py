import numpy as np
from math import sqrt
from collections import defaultdict

def read_input(filename):
    with open(filename) as f:
        sections = f.read().strip().split('\n\n')
        tiles = {}
        for section in sections:
            lines = section.splitlines()
            tile_id = int(lines[0][5:-1])
            tiles[tile_id] = np.array([list(line) for line in lines[1:]])
        return tiles

def get_edges(tile):
    return [
        ''.join(tile[0]),
        ''.join(tile[-1]),
        ''.join(tile[:,0]),
        ''.join(tile[:,-1])
    ]

def get_all_edges(tile):
    edges = get_edges(tile)
    return edges + [edge[::-1] for edge in edges]

def find_corners(tiles):
    edge_matches = defaultdict(int)
    for tile_id, tile in tiles.items():
        edges = get_edges(tile)
        matches = 0
        for other_id, other_tile in tiles.items():
            if tile_id != other_id:
                other_edges = get_all_edges(other_tile)
                for edge in edges:
                    if edge in other_edges or edge[::-1] in other_edges:
                        matches += 1
                        break
        edge_matches[tile_id] = matches
    return [tid for tid, matches in edge_matches.items() if matches == 2]

def get_transformations(tile):
    transforms = []
    for _ in range(4):
        transforms.append(tile)
        transforms.append(np.flipud(tile))
        transforms.append(np.fliplr(tile))
        tile = np.rot90(tile)
    return list(set([tuple(map(tuple, t)) for t in transforms]))

def find_sea_monsters(image):
    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    monster_coords = set()
    for y, row in enumerate(monster):
        for x, char in enumerate(row):
            if char == '#':
                monster_coords.add((y, x))

    image = np.array([list(row) for row in image])
    count = 0
    for transform in get_transformations(image):
        transform = np.array(transform)
        monsters = 0
        for y in range(len(transform) - 2):
            for x in range(len(transform[0]) - 19):
                if all(transform[y+dy][x+dx] == '#' 
                      for dy, dx in monster_coords):
                    monsters += 1
        if monsters > 0:
            return transform, monsters

def assemble_image(tiles):
    size = int(sqrt(len(tiles)))
    grid = [[None] * size for _ in range(size)]
    used = set()
    
    def matches_top(tile1, tile2):
        if tile2 is None:
            return True
        return all(tile1[0][i] == tile2[-1][i] for i in range(len(tile1[0])))
    
    def matches_left(tile1, tile2):
        if tile2 is None:
            return True
        return all(tile1[i][0] == tile2[i][-1] for i in range(len(tile1)))
    
    def place_tile(y, x, tile_id):
        if tile_id in used:
            return False
            
        tile = tiles[tile_id]
        for transform in get_transformations(tile):
            transform = np.array(transform)
            
            # Check top and left matches
            if y > 0 and not matches_top(transform, grid[y-1][x]):
                continue
            if x > 0 and not matches_left(transform, grid[y][x-1]):
                continue
                
            # Check if this placement would prevent future matches
            if y < size-1 and grid[y+1][x] is not None:
                if not matches_top(grid[y+1][x], transform):
                    continue
            if x < size-1 and grid[y][x+1] is not None:
                if not matches_left(grid[y][x+1], transform):
                    continue
                    
            grid[y][x] = transform
            used.add(tile_id)
            return True
        return False
    
    # Place first corner
    corners = find_corners(tiles)
    first_corner = corners[0]
    tile = tiles[first_corner]
    
    # Place first corner in correct orientation
    for transform in get_transformations(tile):
        transform = np.array(transform)
        grid[0][0] = transform
        used.add(first_corner)
        
        # Try to build rest of grid with this orientation
        success = True
        for y in range(size):
            for x in range(size):
                if y == 0 and x == 0:
                    continue
                    
                placed = False
                for tile_id in tiles:
                    if place_tile(y, x, tile_id):
                        placed = True
                        break
                        
                if not placed:
                    success = False
                    break
            if not success:
                break
                
        if success:
            return grid
            
        # Reset for next attempt
        grid = [[None] * size for _ in range(size)]
        used = set()
    
    raise ValueError("Could not assemble image")

def part1(tiles):
    corners = find_corners(tiles)
    result = 1
    for corner in corners:
        result *= corner
    return result

def part2(tiles):
    # Build complete image
    size = int(sqrt(len(tiles)))
    full_image = np.zeros((size * 8, size * 8), dtype=str)
    
    # Remove borders and combine tiles
    assembled = assemble_image(tiles)
    for y in range(size):
        for x in range(size):
            tile = assembled[y][x][1:-1, 1:-1]  # Remove borders
            full_image[y*8:(y+1)*8, x*8:(x+1)*8] = tile
            
    # Find sea monsters and calculate roughness
    image, monsters = find_sea_monsters(full_image)
    return np.sum(image == '#') - monsters * 15

def main():
    """Main program."""
    print("\n--- Day 20: Jurassic Jigsaw ---")
    
    tiles = read_input("2020/input/day20.txt")
    
    result1 = part1(tiles)
    print(f"Part 1: {result1}")
    
    result2 = part2(tiles)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()