def read_input_from_file(filename):
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            if len(numbers) == 2:
                left_list.append(int(numbers[0]))
                right_list.append(int(numbers[1]))

    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    return sum(abs(left - right) for left, right in zip(left_list, right_list))

def calculate_similarity_score(left_list, right_list):
    from collections import Counter

    right_counts = Counter(right_list)
    return sum(number * right_counts[number] for number in left_list if number in right_counts)

def main():
    filename = "2024/Day01/input.txt"
    left_list, right_list = read_input_from_file(filename)

    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Part 1: {total_distance}")

    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Part 2: {similarity_score}")

if __name__ == "__main__":
    main()