<?php

function sumMultiplications($input) {
    $pattern = '/mul\((\d{1,3}),(\d{1,3})\)/'; // Match valid mul(X,Y) instructions
    $matches = [];

    // Find all valid mul(X,Y) instructions
    preg_match_all($pattern, $input, $matches);

    $sum = 0;

    // Process each match
    for ($i = 0; $i < count($matches[0]); $i++) {
        $x = intval($matches[1][$i]); // Extract the first number
        $y = intval($matches[2][$i]); // Extract the second number
        $sum += $x * $y; // Multiply and add to the total sum
    }

    return $sum;
}

// Specify the input file
$inputFile = "input.txt";

// Check if the file exists and read its content
if (file_exists($inputFile)) {
    $input = file_get_contents($inputFile); // Read the file content
    $result = sumMultiplications($input); // Calculate the sum of valid multiplications
    echo "Sum of valid multiplications: " . $result . PHP_EOL;
} else {
    echo "Error: Input file not found!" . PHP_EOL;
}

function sumEnabledMultiplications($input) {
    $patternMul = '/mul\((\d{1,3}),(\d{1,3})\)/'; // Match valid mul(X,Y) instructions
    $patternDo = '/do\(\)/'; // Match do() instruction
    $patternDont = '/don\'?t\(\)/'; // Match don't() instruction
    $matches = [];

    $isEnabled = true; // Start with mul instructions enabled
    $sum = 0;

    // Tokenize the input into meaningful segments
    preg_match_all('/mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'?t\(\)/', $input, $matches, PREG_OFFSET_CAPTURE);

    // Process each matched instruction
    foreach ($matches[0] as $match) {
        $instruction = $match[0];

        if (preg_match($patternDo, $instruction)) {
            $isEnabled = true; // Enable future mul instructions
        } elseif (preg_match($patternDont, $instruction)) {
            $isEnabled = false; // Disable future mul instructions
        } elseif (preg_match($patternMul, $instruction, $mulMatches) && $isEnabled) {
            // If mul is enabled, process the multiplication
            $x = intval($mulMatches[1]);
            $y = intval($mulMatches[2]);
            $sum += $x * $y;
        }
    }

    return $sum;
}

// Specify the input file
$inputFile = "input.txt";

// Check if the file exists and read its content
if (file_exists($inputFile)) {
    $input = file_get_contents($inputFile); // Read the file content
    $result = sumEnabledMultiplications($input); // Calculate the sum of enabled multiplications
    echo "Sum of enabled multiplications: " . $result . PHP_EOL;
} else {
    echo "Error: Input file not found!" . PHP_EOL;
}
