<?php
// File path
$inputFile = 'input.txt';

//--- Day 3: Toboggan Trajectory ---
// Read the input file
$lines = file('input.txt', FILE_IGNORE_NEW_LINES);

// Function to count trees for a given slope
function countTrees($grid, $right, $down) {
    $treeCount = 0;
    $width = strlen($grid[0]); // Width of the grid (repeats horizontally)
    $x = 0; // Horizontal position
    
    // Traverse the grid with the given slope
    for ($y = 0; $y < count($grid); $y += $down) {
        if ($grid[$y][$x % $width] === '#') {
            $treeCount++;
        }
        $x += $right; // Move right by the slope
    }

    return $treeCount;
}

// Part 1: Count trees for slope Right 3, Down 1
$treesPart1 = countTrees($lines, 3, 1);
echo "Part 1: Trees encountered: $treesPart1\n";

//--- Part Two ---
// Part 2: Count trees for multiple slopes
$slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
];

$product = 1;
foreach ($slopes as $slope) {
    [$right, $down] = $slope;
    $trees = countTrees($lines, $right, $down);
    $product *= $trees;
}

echo "Part 2: Product of trees encountered: $product\n";
