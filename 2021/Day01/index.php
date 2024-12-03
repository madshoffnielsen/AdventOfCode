<?php
// File path
$inputFile = 'input.txt';

//--- Day 1: Sonar Sweep ---

// Function to count the number of increases in depth measurements
function countIncreases($inputFile) {
    // Read the file and get the lines
    $lines = file($inputFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $increases = 0;

    // Loop through the measurements, starting from the second one
    for ($i = 1; $i < count($lines); $i++) {
        if ($lines[$i] > $lines[$i - 1]) {
            $increases++;
        }
    }

    return $increases;
}

$result = countIncreases($inputFile);
echo "Number of increases: $result\n";

//--- Part Two ---

// Function to count the number of increases in sums of three-measurement sliding windows
function countSlidingWindowIncreases($inputFile) {
    // Read the file and get the lines
    $lines = file($inputFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $increases = 0;

    // Iterate over the array and calculate the sums of three consecutive measurements
    for ($i = 3; $i < count($lines); $i++) {
        $sum1 = $lines[$i - 3] + $lines[$i - 2] + $lines[$i - 1];
        $sum2 = $lines[$i - 2] + $lines[$i - 1] + $lines[$i];

        // Compare the sums and count increases
        if ($sum2 > $sum1) {
            $increases++;
        }
    }

    return $increases;
}

$result = countSlidingWindowIncreases($inputFile);
echo "Number of sliding window sum increases: $result\n";
