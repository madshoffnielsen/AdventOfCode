import hashlib

def md5_hash(salt, index):
    # Generate the initial MD5 hash of the salt + index
    return hashlib.md5((salt + str(index)).encode('utf-8')).hexdigest()

def stretch_hash(initial_hash):
    # Apply MD5 hash 2016 more times (a total of 2017 MD5 applications)
    hash_result = initial_hash
    for _ in range(2016):
        hash_result = hashlib.md5(hash_result.encode('utf-8')).hexdigest()
    return hash_result

def find_keys(salt, num_keys=64, use_key_stretching=False):
    keys = []
    index = 0
    hash_cache = {}  # Cache to store computed hashes
    stretched_cache = {}  # Cache for stretched hashes
    
    while len(keys) < num_keys:
        # Check if we already have this index's hash
        if index not in hash_cache:
            hash_cache[index] = md5_hash(salt, index)
        
        # Stretch the hash if key stretching is enabled
        if use_key_stretching:
            if index not in stretched_cache:
                stretched_cache[index] = stretch_hash(hash_cache[index])
            hash_value = stretched_cache[index]
        else:
            hash_value = hash_cache[index]
        
        # Find a triplet (three of the same character in a row)
        triplet_char = None
        for i in range(len(hash_value) - 2):
            if hash_value[i] == hash_value[i + 1] == hash_value[i + 2]:
                triplet_char = hash_value[i]
                break

        if triplet_char:
            # Check next 1000 hashes for a quintuplet (five of the same character in a row)
            for future_index in range(index + 1, index + 1001):
                if future_index not in hash_cache:
                    hash_cache[future_index] = md5_hash(salt, future_index)
                
                if future_index not in stretched_cache:
                    stretched_cache[future_index] = stretch_hash(hash_cache[future_index])
                
                future_hash = stretched_cache[future_index] if use_key_stretching else hash_cache[future_index]
                
                if triplet_char * 5 in future_hash:
                    keys.append(index)
                    break

        index += 1

    return keys[-1]

# Solve the problem with the given salt for Part 1
salt = "ngcjuoqr"
result_part1 = find_keys(salt, use_key_stretching=False)
print(f"Part 1: {result_part1}")

# Solve the problem with the given salt for Part 2 (with key stretching)
result_part2 = find_keys(salt, use_key_stretching=True)
print(f"Part 2: {result_part2}")
