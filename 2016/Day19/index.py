from collections import deque

class CircularList:
    def __init__(self, size):
        self.elves = deque(range(1, size + 1))
    
    def rotate(self, n):
        self.elves.rotate(n)
    
    def pop(self):
        return self.elves.popleft()
    
    def __len__(self):
        return len(self.elves)

def part1(n):
    circle = CircularList(n)
    while len(circle) > 1:
        circle.rotate(-1)  # Move to next elf
        circle.pop()       # Remove their presents
    return circle.pop()    # Return last elf standing

def part2(n):
    left = deque(range(1, (n // 2) + 1))
    right = deque(range((n // 2) + 1, n + 1))
    
    while len(left) + len(right) > 1:
        # Remove elf across the circle
        if len(left) > len(right):
            left.pop()
        else:
            right.popleft()
            
        # Rotate the circle
        right.append(left.popleft())
        left.append(right.popleft())
        
    return left[0] if left else right[0]

if __name__ == "__main__":
    INPUT = 3001330
    print(f"Part 1: {part1(INPUT)}")
    print(f"Part 2: {part2(INPUT)}")