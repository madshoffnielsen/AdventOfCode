<?php
// File path
$inputFile = 'input.txt';

//--- Day 1: Report Repair ---
// Read the input from a file called 'input.txt'
// This assumes the numbers are each on a new line in the input file
$numbers = array_map('intval', file('input.txt', FILE_IGNORE_NEW_LINES));

// Function to find the two numbers that sum to 2020
function findTwoNumbers($numbers, $target) {
    $numCount = count($numbers);
    
    for ($i = 0; $i < $numCount; $i++) {
        for ($j = $i + 1; $j < $numCount; $j++) {
            if ($numbers[$i] + $numbers[$j] == $target) {
                return [$numbers[$i], $numbers[$j]];
            }
        }
    }
    
    return null; // No pair found
}

// Target sum is 2020
$target = 2020;

// Find the two numbers that sum to 2020
$pair = findTwoNumbers($numbers, $target);
if ($pair) {
    echo "Part 1: The two numbers are " . $pair[0] . " and " . $pair[1] . ".\n";
    echo "Part 1: Their product is: " . ($pair[0] * $pair[1]) . "\n";
} else {
    echo "Part 1: No two numbers add up to 2020.\n";
}

//--- Part Two ---
// Function to find the three numbers that sum to 2020
function findThreeNumbers($numbers, $target) {
    $numCount = count($numbers);
    
    for ($i = 0; $i < $numCount; $i++) {
        for ($j = $i + 1; $j < $numCount; $j++) {
            for ($k = $j + 1; $k < $numCount; $k++) {
                if ($numbers[$i] + $numbers[$j] + $numbers[$k] == $target) {
                    return [$numbers[$i], $numbers[$j], $numbers[$k]];
                }
            }
        }
    }
    
    return null; // No triplet found
}

// Find the three numbers that sum to 2020
$triplet = findThreeNumbers($numbers, $target);
if ($triplet) {
    echo "Part 2: The three numbers are " . $triplet[0] . ", " . $triplet[1] . " and " . $triplet[2] . ".\n";
    echo "Part 2: Their product is: " . ($triplet[0] * $triplet[1] * $triplet[2]) . "\n";
} else {
    echo "Part 2: No three numbers add up to 2020.\n";
}
