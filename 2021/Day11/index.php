<?php
// File path
$inputFile = 'input.txt';

//--- Day 11: Dumbo Octopus ---
function parseInput($filePath) {
    // Read the input file and parse it into a 2D array of integers
    $lines = file($filePath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $grid = [];
    foreach ($lines as $line) {
        $grid[] = array_map('intval', str_split(trim($line)));
    }
    return $grid;
}

function getNeighbors($x, $y, $grid) {
    // Get all valid neighbors (including diagonals)
    $neighbors = [];
    $directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],          [0, 1],
        [1, -1], [1, 0], [1, 1]
    ];
    foreach ($directions as $dir) {
        $nx = $x + $dir[0];
        $ny = $y + $dir[1];
        if ($nx >= 0 && $nx < count($grid) && $ny >= 0 && $ny < count($grid[0])) {
            $neighbors[] = [$nx, $ny];
        }
    }
    return $neighbors;
}

function simulateStep(&$grid) {
    $flashes = 0;
    $toFlash = [];
    $flashed = [];

    // Increase energy levels by 1
    for ($x = 0; $x < count($grid); $x++) {
        for ($y = 0; $y < count($grid[$x]); $y++) {
            $grid[$x][$y]++;
            if ($grid[$x][$y] > 9) {
                $toFlash[] = [$x, $y];
            }
        }
    }

    // Process flashes
    while (!empty($toFlash)) {
        [$x, $y] = array_pop($toFlash);
        $key = "$x,$y"; // Unique key for flashed tracking
        if (isset($flashed[$key])) {
            continue;
        }
        $flashed[$key] = true;
        $flashes++;

        // Increment neighbors
        foreach (getNeighbors($x, $y, $grid) as [$nx, $ny]) {
            $grid[$nx][$ny]++;
            if ($grid[$nx][$ny] > 9 && !isset($flashed["$nx,$ny"])) {
                $toFlash[] = [$nx, $ny];
            }
        }
    }

    // Reset flashed octopuses to 0
    foreach ($flashed as $key => $_) {
        [$x, $y] = explode(',', $key);
        $grid[$x][$y] = 0;
    }

    return $flashes;
}

function simulateOctopuses($grid, $steps) {
    $totalFlashes = 0;
    for ($i = 0; $i < $steps; $i++) {
        $totalFlashes += simulateStep($grid);
    }
    return $totalFlashes;
}

// Main program
$grid = parseInput($inputFile);
$totalFlashes = simulateOctopuses($grid, 100);

echo "Total flashes after 100 steps: $totalFlashes\n";


//--- Part Two ---
function findSynchronizationStep($grid) {
    $step = 0;
    $totalOctopuses = count($grid) * count($grid[0]);

    while (true) {
        $step++;
        $flashes = simulateStep($grid);
        if ($flashes === $totalOctopuses) {
            return $step;
        }
    }
}

// Main program
$grid = parseInput($inputFile);
$synchronizationStep = findSynchronizationStep($grid);

echo "First synchronization step: $synchronizationStep\n";