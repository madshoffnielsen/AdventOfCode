<?php
// File path
$inputFile = 'input.txt';

//--- Day 2: Password Philosophy ---
// Read the input file
$lines = file('input.txt', FILE_IGNORE_NEW_LINES);

// Function to validate passwords using the old policy (Part 1)
function validatePasswordOldPolicy($line) {
    // Parse the input line
    preg_match('/(\d+)-(\d+) (\w): (\w+)/', $line, $matches);
    [$fullMatch, $min, $max, $char, $password] = $matches;

    // Count occurrences of the character in the password
    $charCount = substr_count($password, $char);

    // Check if it satisfies the policy
    return $charCount >= $min && $charCount <= $max;
}

// Function to validate passwords using the new policy (Part 2)
function validatePasswordNewPolicy($line) {
    // Parse the input line
    preg_match('/(\d+)-(\d+) (\w): (\w+)/', $line, $matches);
    [$fullMatch, $pos1, $pos2, $char, $password] = $matches;

    // Convert positions to 0-based indices
    $pos1--;
    $pos2--;

    // Check if exactly one position contains the character
    $matchesPos1 = $password[$pos1] === $char;
    $matchesPos2 = $password[$pos2] === $char;

    return $matchesPos1 xor $matchesPos2;
}

// Count valid passwords for both policies
$validCountOldPolicy = 0;
$validCountNewPolicy = 0;

foreach ($lines as $line) {
    if (validatePasswordOldPolicy($line)) {
        $validCountOldPolicy++;
    }
    if (validatePasswordNewPolicy($line)) {
        $validCountNewPolicy++;
    }
}

// Output results
echo "Part 1: Valid passwords (old policy): $validCountOldPolicy\n";


//--- Part Two ---
echo "Part 2: Valid passwords (new policy): $validCountNewPolicy\n";
