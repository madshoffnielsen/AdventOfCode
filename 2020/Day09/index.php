<?php
// File path
$inputFile = 'input.txt';

//--- Day 9: Encoding Error ---
// Read the input file
$input = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$numbers = array_map('intval', $input);

// Define the preamble length
$preambleLength = 25; // Change this to 5 for the example input

// Function to check if a number is a valid sum of any two numbers in a given range
function isValid($number, $preamble) {
    $count = count($preamble);
    for ($i = 0; $i < $count - 1; $i++) {
        for ($j = $i + 1; $j < $count; $j++) {
            if ($preamble[$i] + $preamble[$j] === $number) {
                return true;
            }
        }
    }
    return false;
}

// Part 1: Find the first invalid number
$invalidNumber = null;
for ($i = $preambleLength; $i < count($numbers); $i++) {
    $preamble = array_slice($numbers, $i - $preambleLength, $preambleLength);
    if (!isValid($numbers[$i], $preamble)) {
        $invalidNumber = $numbers[$i];
        break;
    }
}

echo "Part 1: First invalid number: $invalidNumber\n";


//--- Part Two ---
// Part 2: Find a contiguous range that sums to the invalid number
function findContiguousSet($numbers, $target) {
    $count = count($numbers);
    for ($start = 0; $start < $count; $start++) {
        $sum = 0;
        for ($end = $start; $end < $count; $end++) {
            $sum += $numbers[$end];
            if ($sum === $target) {
                return array_slice($numbers, $start, $end - $start + 1);
            }
            if ($sum > $target) {
                break;
            }
        }
    }
    return [];
}

$contiguousSet = findContiguousSet($numbers, $invalidNumber);
$min = min($contiguousSet);
$max = max($contiguousSet);
$encryptionWeakness = $min + $max;

echo "Part 2: Encryption weakness: $encryptionWeakness\n";
