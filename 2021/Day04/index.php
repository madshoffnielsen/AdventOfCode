<?php
// File path
$inputFile = 'input.txt';

//--- Day 4: Giant Squid ---

// Function to parse the input and return the drawn numbers and bingo boards
function parseInput($inputFile) {
    $lines = file($inputFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $drawnNumbers = explode(',', array_shift($lines)); // First line contains drawn numbers
    $boards = [];
    
    // Group remaining lines into 5x5 boards
    $currentBoard = [];
    foreach ($lines as $line) {
        $numbers = preg_split('/\s+/', $line); // Split line by spaces
        $currentBoard[] = $numbers;
        
        // If we have a complete board (5 rows), add it to the boards list
        if (count($currentBoard) === 5) {
            $boards[] = $currentBoard;
            $currentBoard = [];
        }
    }
    
    return [$drawnNumbers, $boards];
}

// Function to check if a board has won (row or column)
function isWinner($board) {
    // Check each row
    foreach ($board as $row) {
        if (count(array_filter($row, fn($x) => $x === 'X')) === 5) {
            return true;
        }
    }
    
    // Check each column
    for ($col = 0; $col < 5; $col++) {
        $count = 0;
        for ($row = 0; $row < 5; $row++) {
            if ($board[$row][$col] === 'X') {
                $count++;
            }
        }
        if ($count === 5) {
            return true;
        }
    }
    
    return false;
}

// Function to calculate the score of a winning board
function calculateScore($board, $lastDrawnNumber) {
    $unmarkedSum = 0;
    
    // Sum all unmarked numbers
    foreach ($board as $row) {
        foreach ($row as $num) {
            if ($num !== 'X') {
                $unmarkedSum += $num;
            }
        }
    }
    
    return $unmarkedSum * $lastDrawnNumber;
}

// Main function to simulate the Bingo game
function playBingo($inputFile) {
    // Parse the input file
    list($drawnNumbers, $boards) = parseInput($inputFile);
    
    // Mark boards as we draw numbers
    foreach ($drawnNumbers as $drawnNumber) {
        foreach ($boards as &$board) {
            // Mark the number on the board
            foreach ($board as &$row) {
                foreach ($row as &$num) {
                    if ($num == $drawnNumber) {
                        $num = 'X'; // Mark the number
                    }
                }
            }
            
            // Check if the board has won
            if (isWinner($board)) {
                return calculateScore($board, $drawnNumber); // Return score of the winning board
            }
        }
    }
}

// Play the Bingo game and display the result
$result = playBingo($inputFile);
echo "The final score of the first winning board is: $result\n";


//--- Part Two ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));
$lines = explode("\n",$input);

$balls = explode(",",$lines[0]);
$b = (sizeof($lines)-1)/6;
for($i=0;$i<$b;$i++) {
	for($l=0;$l<5;$l++) {
		$line = $lines[2+($i*6)+$l];
		for($j=0;$j<5;$j++) {
			$ball = (int)substr($line,$j*3,2);
			$board[$i]["row"][$l][] = $ball;
			$board[$i]["col"][$j][] = $ball;
		}
	}
}

$copy = array_merge($board);
$winning_board = -1;
$winning_ball = -1;
$winning_dir = "";
$completed_boards = [];
foreach($balls as $ball) {
	for($i=0;$i<sizeof($board);$i++){
		for($l=0;$l<5;$l++) {
			$row = 0; $col = 0;
			for($j=0;$j<5;$j++) {
				if($board[$i]["row"][$l][$j] == $ball) {
					$copy[$i]["row"][$l][$j] = "X";
				}
				if($board[$i]["col"][$l][$j] == $ball) {
					$copy[$i]["col"][$l][$j] = "X";
				}
				if($copy[$i]["row"][$l][$j] == "X") {
					$row++;
				}
				if($copy[$i]["col"][$l][$j] == "X") {
					$col++;
				}
			}
			if($row == 5 || $col == 5) {
				if(!in_array($i,$completed_boards)) {
					$completed_boards[] = $i;
					if(sizeof($completed_boards) == sizeof($board)) {
						$winning_board = $i;
						$winning_ball = $ball;
						$winning_dir = ($row == 5) ? "row" : "col";
						break 3;
					}
				}
			}
		}
	}
}

$sum = 0;
for($l=0;$l<5;$l++) {
	for($j=0;$j<5;$j++) {
		if($copy[$winning_board][$winning_dir][$l][$j] !== "X") {
			$sum += $copy[$winning_board][$winning_dir][$l][$j];
		}
	}
}
$answer = $sum * $winning_ball;
		
echo "Answer: {$answer}\n";
