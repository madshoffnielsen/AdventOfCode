<?php
// File path
$inputFile = 'input.txt';

//--- Day 10: Adapter Array ---
// Read the input file
$input = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$adapters = array_map('intval', $input);

// Add outlet and device's built-in adapter
$adapters[] = 0; // Outlet
$adapters[] = max($adapters) + 3; // Device's adapter

// Sort the adapters
sort($adapters);

// Part 1: Find 1-jolt and 3-jolt differences
$oneJoltDiff = 0;
$threeJoltDiff = 0;

for ($i = 1; $i < count($adapters); $i++) {
    $difference = $adapters[$i] - $adapters[$i - 1];
    if ($difference === 1) {
        $oneJoltDiff++;
    } elseif ($difference === 3) {
        $threeJoltDiff++;
    }
}

$part1 = $oneJoltDiff * $threeJoltDiff;
echo "Part 1: Product of 1-jolt and 3-jolt differences: $part1\n";


//--- Part Two ---
// Part 2: Count all possible arrangements
$paths = array_fill(0, max($adapters) + 1, 0);
$paths[0] = 1; // There's exactly one way to connect to the outlet (joltage 0)

foreach ($adapters as $adapter) {
    for ($diff = 1; $diff <= 3; $diff++) {
        if (isset($paths[$adapter - $diff])) {
            $paths[$adapter] += $paths[$adapter - $diff];
        }
    }
}

$part2 = $paths[max($adapters)];
echo "Part 2: Total distinct arrangements: $part2\n";
