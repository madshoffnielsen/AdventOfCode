import heapq

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return [[int(char) for char in line.strip()] for line in file if line.strip()]

def dijkstra(risk_map):
    rows, cols = len(risk_map), len(risk_map[0])
    pq = [(0, 0, 0)]  # (risk, x, y)
    risk_levels = [[float('inf')] * cols for _ in range(rows)]
    risk_levels[0][0] = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while pq:
        current_risk, x, y = heapq.heappop(pq)
        
        if (x, y) == (rows - 1, cols - 1):
            return current_risk
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_risk = current_risk + risk_map[nx][ny]
                if new_risk < risk_levels[nx][ny]:
                    risk_levels[nx][ny] = new_risk
                    heapq.heappush(pq, (new_risk, nx, ny))
    
    return -1

def generate_full_map(original_map):
    rows, cols = len(original_map), len(original_map[0])
    full_map = [[0] * (cols * 5) for _ in range(rows * 5)]
    
    for i in range(rows * 5):
        for j in range(cols * 5):
            original_risk = original_map[i % rows][j % cols]
            new_risk = original_risk + (i // rows) + (j // cols)
            full_map[i][j] = (new_risk - 1) % 9 + 1
    
    return full_map

def main():
    print("\n--- Day 15: Chiton ---")
    input_file = '2021/input/day15.txt'
    risk_map = parse_input(input_file)
    lowest_risk = dijkstra(risk_map)
    print(f"Part 1: {lowest_risk}")

    full_map = generate_full_map(risk_map)
    lowest_risk_full = dijkstra(full_map)
    print(f"Part 2: {lowest_risk_full}")

if __name__ == "__main__":
    main()
