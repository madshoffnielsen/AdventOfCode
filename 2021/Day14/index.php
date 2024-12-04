<?php
// File path
$inputFile = 'input.txt';

//--- Day 14: Extended Polymerization ---
function parseInput($filePath) {
    $lines = file($filePath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $template = array_shift($lines);
    $rules = [];

    foreach ($lines as $line) {
        [$pair, $insert] = explode(" -> ", $line);
        $rules[$pair] = $insert;
    }

    return [$template, $rules];
}

function simulatePolymerization($template, $rules, $steps) {
    // Initialize pair counts and element counts
    $pairCounts = [];
    $elementCounts = [];

    // Populate the initial pair counts and element counts
    for ($i = 0; $i < strlen($template) - 1; $i++) {
        $pair = $template[$i] . $template[$i + 1];
        $pairCounts[$pair] = ($pairCounts[$pair] ?? 0) + 1;
    }

    foreach (str_split($template) as $char) {
        $elementCounts[$char] = ($elementCounts[$char] ?? 0) + 1;
    }

    // Simulate the process for the given number of steps
    for ($step = 1; $step <= $steps; $step++) {
        $newPairCounts = [];

        foreach ($pairCounts as $pair => $count) {
            if (isset($rules[$pair])) {
                $insert = $rules[$pair];
                $newPair1 = $pair[0] . $insert;
                $newPair2 = $insert . $pair[1];

                // Update new pairs
                $newPairCounts[$newPair1] = ($newPairCounts[$newPair1] ?? 0) + $count;
                $newPairCounts[$newPair2] = ($newPairCounts[$newPair2] ?? 0) + $count;

                // Update element counts
                $elementCounts[$insert] = ($elementCounts[$insert] ?? 0) + $count;
            }
        }

        $pairCounts = $newPairCounts;
    }

    // Calculate the difference between most and least common elements
    $maxCount = max($elementCounts);
    $minCount = min($elementCounts);

    return $maxCount - $minCount;
}

// Main program
[$template, $rules] = parseInput($inputFile);
$result = simulatePolymerization($template, $rules, 10);
echo "Difference between most and least common elements after 10 steps: $result\n";


//--- Part Two ---

// Main program
[$template, $rules] = parseInput($inputFile);
$result = simulatePolymerization($template, $rules, 40);
echo "Difference between most and least common elements after 40 steps: $result\n";
