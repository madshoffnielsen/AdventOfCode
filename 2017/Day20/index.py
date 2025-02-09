import re

class Particle:
    def __init__(self, id, position, velocity, acceleration):
        self.id = id
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def update(self):
        self.velocity = [v + a for v, a in zip(self.velocity, self.acceleration)]
        self.position = [p + v for p, v in zip(self.position, self.velocity)]

    def distance(self):
        return sum(abs(p) for p in self.position)

def parse_input(file_path):
    particles = []
    with open(file_path) as f:
        for id, line in enumerate(f):
            p, v, a = re.findall(r'<([^>]+)>', line)
            position = list(map(int, p.split(',')))
            velocity = list(map(int, v.split(',')))
            acceleration = list(map(int, a.split(',')))
            particles.append(Particle(id, position, velocity, acceleration))
    return particles

def part1(particles):
    min_acceleration = min(particles, key=lambda p: sum(map(abs, p.acceleration)))
    return min_acceleration.id

def part2(particles):
    for _ in range(1000):  # Arbitrary large number of steps to ensure collisions are resolved
        positions = {}
        for particle in particles:
            particle.update()
            pos_tuple = tuple(particle.position)
            if pos_tuple in positions:
                positions[pos_tuple].append(particle)
            else:
                positions[pos_tuple] = [particle]
        
        particles = [p for pos in positions.values() if len(pos) == 1 for p in pos]
    
    return len(particles)

if __name__ == "__main__":
    particles = parse_input("2017/Day20/input.txt")
    print("Part 1:", part1(particles))
    particles = parse_input("2017/Day20/input.txt")  # Re-parse to reset particles for part 2
    print("Part 2:", part2(particles))