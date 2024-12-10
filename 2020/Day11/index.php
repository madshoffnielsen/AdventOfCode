<?php
// File path
$inputFile = 'input.txt';

//--- Day 11: Seating System ---
// Read the input file
$input = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$grid = array_map('str_split', $input);

// Helper function to count occupied seats around a given position
function countAdjacentOccupied($grid, $row, $col) {
    $directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1], [1, 0], [1, 1]
    ];
    $occupied = 0;

    foreach ($directions as [$dx, $dy]) {
        $r = $row + $dx;
        $c = $col + $dy;
        if (isset($grid[$r][$c]) && $grid[$r][$c] === '#') {
            $occupied++;
        }
    }

    return $occupied;
}

// Helper function to count visible occupied seats (for Part 2)
function countVisibleOccupied($grid, $row, $col) {
    $directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1], [1, 0], [1, 1]
    ];
    $occupied = 0;

    foreach ($directions as [$dx, $dy]) {
        $r = $row;
        $c = $col;

        while (true) {
            $r += $dx;
            $c += $dy;
            if (!isset($grid[$r][$c])) {
                break;
            }
            if ($grid[$r][$c] === 'L') {
                break;
            }
            if ($grid[$r][$c] === '#') {
                $occupied++;
                break;
            }
        }
    }

    return $occupied;
}

// Simulation function
function simulateSeating($grid, $tolerance, $useVisible) {
    $rows = count($grid);
    $cols = count($grid[0]);

    while (true) {
        $newGrid = $grid;
        $changed = false;

        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                if ($grid[$r][$c] === '.') {
                    continue;
                }

                $occupied = $useVisible
                    ? countVisibleOccupied($grid, $r, $c)
                    : countAdjacentOccupied($grid, $r, $c);

                if ($grid[$r][$c] === 'L' && $occupied === 0) {
                    $newGrid[$r][$c] = '#';
                    $changed = true;
                } elseif ($grid[$r][$c] === '#' && $occupied >= $tolerance) {
                    $newGrid[$r][$c] = 'L';
                    $changed = true;
                }
            }
        }

        if (!$changed) {
            break;
        }

        $grid = $newGrid;
    }

    // Count occupied seats
    $occupiedSeats = 0;
    foreach ($grid as $row) {
        $occupiedSeats += substr_count(implode('', $row), '#');
    }

    return $occupiedSeats;
}

// Part 1
$part1 = simulateSeating($grid, 4, false);
echo "Part 1: Occupied seats after stabilization: $part1\n";


//--- Part Two ---
// Part 2
$part2 = simulateSeating($grid, 5, true);
echo "Part 2: Occupied seats after stabilization: $part2\n";
