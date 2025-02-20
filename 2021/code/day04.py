def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    drawn_numbers = lines[0].split(',')
    boards = []
    current_board = []

    for line in lines[1:]:
        if line == '':
            if current_board:
                boards.append(current_board)
                current_board = []
        else:
            current_board.append(line.split())

    if current_board:
        boards.append(current_board)

    return drawn_numbers, boards

def is_winner(board):
    # Check rows
    for row in board:
        if all(num == 'X' for num in row):
            return True

    # Check columns
    for col in range(5):
        if all(row[col] == 'X' for row in board):
            return True

    return False

def calculate_score(board, last_drawn_number):
    unmarked_sum = sum(int(num) for row in board for num in row if num != 'X')
    return unmarked_sum * int(last_drawn_number)

def mark_number(board, number):
    for row in board:
        for i in range(len(row)):
            if row[i] == number:
                row[i] = 'X'

def play_bingo(drawn_numbers, boards):
    for drawn_number in drawn_numbers:
        for board in boards:
            mark_number(board, drawn_number)
            if is_winner(board):
                return calculate_score(board, drawn_number)

def play_bingo_last_winner(drawn_numbers, boards):
    completed_boards = set()
    last_score = 0

    for drawn_number in drawn_numbers:
        for board_index, board in enumerate(boards):
            if board_index in completed_boards:
                continue

            mark_number(board, drawn_number)
            if is_winner(board):
                completed_boards.add(board_index)
                last_score = calculate_score(board, drawn_number)

    return last_score

def main():
    print("\n--- Day 4: Giant Squid ---")
    drawn_numbers, boards = parse_input('2021/input/day04.txt')
    
    # Part 1
    result = play_bingo(drawn_numbers, boards)
    print(f"Part 1: {result}")

    # Part 2
    result_last_winner = play_bingo_last_winner(drawn_numbers, boards)
    print(f"Part 2: {result_last_winner}")

if __name__ == "__main__":
    main()