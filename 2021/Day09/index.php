<?php
// File path
$inputFile = 'input.txt';

//--- Day 9: Smoke Basin ---
function calculateRiskLevels($filename) {
    // Read the input file into a 2D array
    $heightmap = array_map('str_split', file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES));

    $rows = count($heightmap);
    $cols = count($heightmap[0]);
    $totalRiskLevel = 0;

    // Iterate over each cell in the heightmap
    for ($i = 0; $i < $rows; $i++) {
        for ($j = 0; $j < $cols; $j++) {
            $current = $heightmap[$i][$j];

            // Check adjacent cells
            $isLowPoint = true;

            // Up
            if ($i > 0 && $heightmap[$i - 1][$j] <= $current) {
                $isLowPoint = false;
            }

            // Down
            if ($i < $rows - 1 && $heightmap[$i + 1][$j] <= $current) {
                $isLowPoint = false;
            }

            // Left
            if ($j > 0 && $heightmap[$i][$j - 1] <= $current) {
                $isLowPoint = false;
            }

            // Right
            if ($j < $cols - 1 && $heightmap[$i][$j + 1] <= $current) {
                $isLowPoint = false;
            }

            // If it's a low point, calculate its risk level
            if ($isLowPoint) {
                $riskLevel = $current + 1; // Risk level = height + 1
                $totalRiskLevel += $riskLevel;
            }
        }
    }

    return $totalRiskLevel;
}

// Calculate the total risk level
$result = calculateRiskLevels($inputFile);

echo "Total risk level: $result\n";


//--- Part Two ---
function findBasins($filename) {
    // Read the input file into a 2D array
    $heightmap = array_map('str_split', file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES));

    $rows = count($heightmap);
    $cols = count($heightmap[0]);
    $basins = [];
    $visited = array_fill(0, $rows, array_fill(0, $cols, false));

    // Directions for moving up, down, left, right
    $directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

    // Helper function to perform DFS and find all locations in a basin
    function floodFill($i, $j, $heightmap, &$visited, $rows, $cols) {
        // Stack for DFS
        $stack = [[$i, $j]];
        $size = 0;

        while (count($stack) > 0) {
            [$x, $y] = array_pop($stack);
            if ($visited[$x][$y] || $heightmap[$x][$y] == 9) {
                continue;
            }

            // Mark the location as visited
            $visited[$x][$y] = true;
            $size++;

            // Check all 4 adjacent directions
            foreach ([[-1, 0], [1, 0], [0, -1], [0, 1]] as $direction) {
                $newX = $x + $direction[0];
                $newY = $y + $direction[1];

                // If it's within bounds and not visited and not a '9'
                if ($newX >= 0 && $newX < $rows && $newY >= 0 && $newY < $cols && !$visited[$newX][$newY] && $heightmap[$newX][$newY] != 9) {
                    $stack[] = [$newX, $newY];
                }
            }
        }

        return $size;
    }

    // Find all basins by exploring each low point
    for ($i = 0; $i < $rows; $i++) {
        for ($j = 0; $j < $cols; $j++) {
            // Check if the point is a low point
            $current = $heightmap[$i][$j];
            $isLowPoint = true;

            // Check adjacent points
            foreach ($directions as $direction) {
                $newX = $i + $direction[0];
                $newY = $j + $direction[1];

                if ($newX >= 0 && $newX < $rows && $newY >= 0 && $newY < $cols) {
                    if ($heightmap[$newX][$newY] <= $current) {
                        $isLowPoint = false;
                        break;
                    }
                }
            }

            // If it's a low point, find the basin size
            if ($isLowPoint) {
                $basinSize = floodFill($i, $j, $heightmap, $visited, $rows, $cols);
                $basins[] = $basinSize;
            }
        }
    }

    // Sort basins in descending order
    rsort($basins);

    // Multiply the sizes of the three largest basins
    $result = $basins[0] * $basins[1] * $basins[2];
    return $result;
}

// Find the product of the sizes of the three largest basins
$result = findBasins($inputFile);

echo "The product of the three largest basins is: $result\n";
