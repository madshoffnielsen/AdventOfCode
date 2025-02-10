from collections import namedtuple
import heapq

State = namedtuple('State', ['mana_spent', 'player_hp', 'player_mana', 'boss_hp', 'shield', 'poison', 'recharge'])

def read_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return {'hp': int(lines[0].split(': ')[1]), 'damage': int(lines[1].split(': ')[1])}

def apply_effects(state):
    boss_hp = state.boss_hp - (3 if state.poison > 0 else 0)
    mana = state.player_mana + (101 if state.recharge > 0 else 0)
    return State(state.mana_spent, state.player_hp, mana, boss_hp,
                max(0, state.shield - 1), max(0, state.poison - 1), max(0, state.recharge - 1))

def find_minimum_mana(boss_stats, hard_mode=False):
    queue = [(0, State(0, 50, 500, boss_stats['hp'], 0, 0, 0))]
    seen = set()
    spells = [
        (53, 4, 0, None, 0),     # Magic Missile
        (73, 2, 2, None, 0),     # Drain
        (113, 0, 0, 'shield', 6),
        (173, 0, 0, 'poison', 6),
        (229, 0, 0, 'recharge', 5)
    ]
    
    while queue:
        _, state = heapq.heappop(queue)
        
        # Player turn
        if hard_mode:
            state = state._replace(player_hp=state.player_hp - 1)
            if state.player_hp <= 0:
                continue
        
        # Apply effects before player turn
        state = apply_effects(state)
        if state.boss_hp <= 0:
            return state.mana_spent
            
        # Cast spell
        armor = 7 if state.shield > 0 else 0
        for cost, damage, heal, effect, duration in spells:
            if cost > state.player_mana:
                continue
            if (effect == 'shield' and state.shield > 0) or \
               (effect == 'poison' and state.poison > 0) or \
               (effect == 'recharge' and state.recharge > 0):
                continue
                
            # Apply spell
            new_state = State(
                state.mana_spent + cost,
                state.player_hp + heal,
                state.player_mana - cost,
                state.boss_hp - damage,
                duration if effect == 'shield' else state.shield,
                duration if effect == 'poison' else state.poison,
                duration if effect == 'recharge' else state.recharge
            )
            
            # Apply effects before boss turn
            new_state = apply_effects(new_state)
            if new_state.boss_hp <= 0:
                return new_state.mana_spent
                
            # Boss turn
            new_state = new_state._replace(
                player_hp=new_state.player_hp - max(1, boss_stats['damage'] - (7 if new_state.shield > 0 else 0))
            )
            
            if new_state.player_hp <= 0:
                continue
                
            state_tuple = (new_state.player_hp, new_state.player_mana, new_state.boss_hp,
                          new_state.shield, new_state.poison, new_state.recharge)
            if state_tuple not in seen:
                seen.add(state_tuple)
                heapq.heappush(queue, (new_state.mana_spent, new_state))
    
    return float('inf')

def main():
    boss_stats = read_input("2015/Day22/input.txt")
    print(f"Part 1: {find_minimum_mana(boss_stats)}")
    print(f"Part 2: {find_minimum_mana(boss_stats, hard_mode=True)}")

if __name__ == "__main__":
    main()