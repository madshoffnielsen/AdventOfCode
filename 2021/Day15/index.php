<?php
// File path
$inputFile = 'input.txt';

//--- Day 15: Chiton ---
function parseInput($filePath) {
    $lines = file($filePath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $map = array_map('str_split', $lines); // Convert each line to an array of digits
    return $map;
}

function dijkstra($map) {
    $rows = count($map);
    $cols = count($map[0]);

    // Priority queue (min-heap) initialized with the starting position (0, 0)
    $pq = new SplPriorityQueue();
    $pq->insert([0, 0], 0); // [x, y], priority: 0 (starting point)
    
    // Risk levels array, initialized to infinity
    $risk = array_fill(0, $rows, array_fill(0, $cols, PHP_INT_MAX));
    $risk[0][0] = 0; // Starting point has 0 risk

    // Direction vectors for moving up, down, left, right
    $directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    while (!$pq->isEmpty()) {
        list($x, $y) = $pq->extract();
        $currentRisk = $risk[$x][$y];

        // If we reached the bottom-right corner, return the risk level
        if ($x === $rows - 1 && $y === $cols - 1) {
            return $currentRisk;
        }

        // Explore all adjacent cells (up, down, left, right)
        foreach ($directions as [$dx, $dy]) {
            $nx = $x + $dx;
            $ny = $y + $dy;

            // Skip out-of-bounds positions
            if ($nx < 0 || $nx >= $rows || $ny < 0 || $ny >= $cols) {
                continue;
            }

            // Calculate the new risk level
            $newRisk = $currentRisk + $map[$nx][$ny];

            // If the new risk level is lower, update and add to the priority queue
            if ($newRisk < $risk[$nx][$ny]) {
                $risk[$nx][$ny] = $newRisk;
                $pq->insert([$nx, $ny], -$newRisk); // Min-heap uses negative priority for lower risk
            }
        }
    }

    return -1; // Should never reach here if there's a valid path
}

// Main program
$map = parseInput($inputFile);
$lowestRisk = dijkstra($map);
echo "Lowest total risk of any path: $lowestRisk\n";


//--- Part Two ---
// Function to generate the full 5x5 map from the original map
function generateFullMap($originalMap) {
    $rows = count($originalMap);
    $cols = count($originalMap[0]);
    $fullMap = [];

    // Expand the map
    for ($i = 0; $i < $rows * 5; $i++) {
        $fullMapRow = [];
        for ($j = 0; $j < $cols * 5; $j++) {
            $originalRisk = $originalMap[$i % $rows][$j % $cols];
            // Calculate the new risk level
            $newRisk = $originalRisk + intdiv($i, $rows) + intdiv($j, $cols);
            // Wrap around if the risk level is greater than 9
            $fullRisk = (($newRisk - 1) % 9) + 1;
            $fullMapRow[] = $fullRisk;
        }
        $fullMap[] = $fullMapRow;
    }

    return $fullMap;
}

// Function to read the input from the file and parse it into a 2D array
function readInputFromFile($filename) {
    $lines = file($filename, FILE_IGNORE_NEW_LINES);
    $map = [];

    foreach ($lines as $line) {
        $map[] = str_split($line);  // Convert each line into an array of digits
    }

    return $map;
}

// Read the input map from the file
$originalMap = readInputFromFile('input.txt');

// Generate the full 5x5 map from the original map
$fullMap = generateFullMap($originalMap);

// Find the minimum risk path using Dijkstra's algorithm
$lowestRisk = dijkstra($fullMap);

// Output the result
echo "Lowest total risk of any path: " . $lowestRisk . "\n";