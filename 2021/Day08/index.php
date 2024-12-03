<?php
// File path
$inputFile = 'input.txt';

//--- Day 8: Seven Segment Search ---
function countEasyDigits($inputFile) {
    // Read the file contents
    $lines = file($inputFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    
    // Initialize the count for digits 1, 4, 7, and 8
    $easyDigitCount = 0;

    // Unique segment lengths for digits 1, 4, 7, and 8
    $uniqueSegmentLengths = [2, 4, 3, 7];

    // Process each line
    foreach ($lines as $line) {
        // Split into signal patterns and output values
        list(, $outputValues) = explode(' | ', $line);
        
        // Split output values into individual signals
        $outputSignals = explode(' ', $outputValues);

        // Count signals with unique segment lengths
        foreach ($outputSignals as $signal) {
            if (in_array(strlen($signal), $uniqueSegmentLengths)) {
                $easyDigitCount++;
            }
        }
    }

    return $easyDigitCount;
}

// Input file containing the signal patterns and output values
$inputFile = 'input.txt';

// Count the occurrences of digits 1, 4, 7, or 8 in the output values
$result = countEasyDigits($inputFile);

echo "Number of times digits 1, 4, 7, or 8 appear: $result\n";


//--- Part Two ---
function decodeAndSum($inputFile) {
    $lines = file($inputFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $totalSum = 0;

    foreach ($lines as $line) {
        // Split the input into patterns and output values
        list($patterns, $outputs) = explode(' | ', $line);
        $patterns = explode(' ', $patterns);
        $outputs = explode(' ', $outputs);

        // Map the patterns to digits
        $mapping = deduceMapping($patterns);

        // Decode the output values
        $decodedValue = decodeOutput($outputs, $mapping);

        // Add to the total sum
        $totalSum += $decodedValue;
    }

    return $totalSum;
}

function deduceMapping($patterns) {
    // Sort all patterns alphabetically
    $sortedPatterns = array_map(function($pattern) {
        $chars = str_split($pattern);
        sort($chars);
        return implode('', $chars);
    }, $patterns);

    // Find the unique lengths for digits 1, 4, 7, 8
    $byLength = [];
    foreach ($sortedPatterns as $pattern) {
        $byLength[strlen($pattern)][] = $pattern;
    }

    // Map known lengths
    $mapping = [];
    $reverseMapping = [];
    $reverseMapping[1] = $byLength[2][0]; // Digit 1
    $reverseMapping[4] = $byLength[4][0]; // Digit 4
    $reverseMapping[7] = $byLength[3][0]; // Digit 7
    $reverseMapping[8] = $byLength[7][0]; // Digit 8

    // Deduce other digits
    foreach ($byLength[6] as $pattern) { // Length 6: 0, 6, or 9
        if (containsAll($pattern, $reverseMapping[4])) {
            $reverseMapping[9] = $pattern;
        } elseif (containsAll($pattern, $reverseMapping[7])) {
            $reverseMapping[0] = $pattern;
        } else {
            $reverseMapping[6] = $pattern;
        }
    }
    foreach ($byLength[5] as $pattern) { // Length 5: 2, 3, or 5
        if (containsAll($pattern, $reverseMapping[7])) {
            $reverseMapping[3] = $pattern;
        } elseif (containsAll($reverseMapping[6], $pattern)) {
            $reverseMapping[5] = $pattern;
        } else {
            $reverseMapping[2] = $pattern;
        }
    }

    // Invert the mapping for easy decoding
    foreach ($reverseMapping as $digit => $pattern) {
        $mapping[$pattern] = $digit;
    }

    return $mapping;
}

function containsAll($pattern, $subset) {
    $patternChars = str_split($pattern);
    $subsetChars = str_split($subset);
    return count(array_diff($subsetChars, $patternChars)) === 0;
}

function decodeOutput($outputs, $mapping) {
    $decodedDigits = '';
    foreach ($outputs as $output) {
        $chars = str_split($output);
        sort($chars);
        $sortedOutput = implode('', $chars);
        $decodedDigits .= $mapping[$sortedOutput];
    }
    return intval($decodedDigits);
}

// Input file containing the signal patterns and output values
$inputFile = 'input.txt';

// Decode and sum all output values
$result = decodeAndSum($inputFile);

echo "Sum of all output values: $result\n";