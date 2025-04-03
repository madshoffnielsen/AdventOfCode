from typing import List, Tuple, Optional
from dataclasses import dataclass
from itertools import combinations

@dataclass
class Hailstone:
    px: int  # position x
    py: int  # position y
    pz: int  # position z
    vx: int  # velocity x
    vy: int  # velocity y
    vz: int  # velocity z

def read_input(file_path: str) -> List[Hailstone]:
    """Read hailstone positions and velocities."""
    hailstones = []
    with open(file_path) as f:
        for line in f:
            pos, vel = line.strip().split(' @ ')
            px, py, pz = map(int, pos.split(', '))
            vx, vy, vz = map(int, vel.split(', '))
            hailstones.append(Hailstone(px, py, pz, vx, vy, vz))
    return hailstones

def find_intersection_2d(h1: Hailstone, h2: Hailstone) -> Optional[Tuple[float, float]]:
    """Find intersection point of two hailstones in 2D (xy plane)."""
    # Convert to line equation ax + by = c
    a1 = h1.vy
    b1 = -h1.vx
    c1 = h1.vy * h1.px - h1.vx * h1.py
    
    a2 = h2.vy
    b2 = -h2.vx
    c2 = h2.vy * h2.px - h2.vx * h2.py
    
    # Check if parallel
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    
    # Find intersection point
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    
    # Check if intersection is in the future for both hailstones
    if ((x - h1.px) * h1.vx < 0 or 
        (y - h1.py) * h1.vy < 0 or
        (x - h2.px) * h2.vx < 0 or 
        (y - h2.py) * h2.vy < 0):
        return None
        
    return (x, y)

def part1(hailstones: List[Hailstone], min_pos: int = 200000000000000, 
          max_pos: int = 400000000000000) -> int:
    """Count intersections within test area."""
    count = 0
    for h1, h2 in combinations(hailstones, 2):
        intersection = find_intersection_2d(h1, h2)
        if intersection:
            x, y = intersection
            if min_pos <= x <= max_pos and min_pos <= y <= max_pos:
                count += 1
    return count

def solve_system(hailstones: List[Hailstone]) -> int:
    """Solve system of equations using Z3."""
    from z3 import Solver, Int, Real
    
    s = Solver()
    x, y, z = Real('x'), Real('y'), Real('z')
    vx, vy, vz = Real('vx'), Real('vy'), Real('vz')
    
    # We only need 3 hailstones to find the solution
    for i, h in enumerate(hailstones[:3]):
        t = Real(f't{i}')
        s.add(t >= 0)
        s.add(x + vx * t == h.px + h.vx * t)
        s.add(y + vy * t == h.py + h.vy * t)
        s.add(z + vz * t == h.pz + h.vz * t)
    
    if s.check():
        m = s.model()
        return sum(int(str(m.eval(v))) for v in (x, y, z))
    return 0

def part2(hailstones: List[Hailstone]) -> int:
    """Find sum of coordinates where rock needs to be thrown from."""
    return solve_system(hailstones)

def main():
    """Main program."""
    print("\n--- Day 24: Never Tell Me The Odds ---")
    
    hailstones = read_input("2023/Day24/input.txt")
    
    result1 = part1(hailstones)
    print(f"Part 1: {result1}")
    
    result2 = part2(hailstones)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()