from itertools import combinations

def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    boss_stats = {}
    for line in lines:
        parts = line.strip().split(': ')
        boss_stats[parts[0]] = int(parts[1])
    return boss_stats

def simulate_battle(player, boss):
    player_hp, player_damage, player_armor = player
    boss_hp, boss_damage, boss_armor = boss
    player_effective_damage = max(1, player_damage - boss_armor)
    boss_effective_damage = max(1, boss_damage - player_armor)
    
    while True:
        boss_hp -= player_effective_damage
        if boss_hp <= 0:
            return True
        player_hp -= boss_effective_damage
        if player_hp <= 0:
            return False

def find_optimal_cost(boss_stats, find_max_cost=False):
    weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
    armors = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
    rings = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]
    
    best_cost = float('inf') if not find_max_cost else 0
    
    for weapon in weapons:
        for armor in armors:
            for ring1, ring2 in combinations(rings, 2):
                cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
                damage = weapon[1] + armor[1] + ring1[1] + ring2[1]
                player_armor = weapon[2] + armor[2] + ring1[2] + ring2[2]
                player = (100, damage, player_armor)
                boss = (boss_stats['Hit Points'], boss_stats['Damage'], boss_stats['Armor'])
                
                if simulate_battle(player, boss):
                    if not find_max_cost:
                        best_cost = min(best_cost, cost)
                else:
                    if find_max_cost:
                        best_cost = max(best_cost, cost)
    
    return best_cost

def main():
    boss_stats = read_input("2015/Day21/input.txt")
    print(f"Part 1: {find_optimal_cost(boss_stats)}")
    print(f"Part 2: {find_optimal_cost(boss_stats, find_max_cost=True)}")

if __name__ == "__main__":
    main()