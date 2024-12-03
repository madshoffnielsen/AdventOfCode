<?php
// File path
$inputFile = 'input.txt';

//--- Day 10: Syntax Scoring ---
function calculateSyntaxErrorScore($filename) {
    // Read the input file into an array of lines
    $lines = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

    // Define a mapping of closing characters to points
    $scoreMap = [
        ')' => 3,
        ']' => 57,
        '}' => 1197,
        '>' => 25137
    ];

    // Define the matching pairs for brackets
    $matchingBrackets = [
        ')' => '(',
        ']' => '[',
        '}' => '{',
        '>' => '<'
    ];

    $totalScore = 0;

    // Process each line
    foreach ($lines as $line) {
        $stack = [];

        // Traverse each character in the line
        $isCorrupted = false;
        foreach (str_split($line) as $char) {
            // If it's an opening bracket, push to the stack
            if (in_array($char, ['(', '[', '{', '<'])) {
                $stack[] = $char;
            }
            // If it's a closing bracket, check if it matches the top of the stack
            elseif (in_array($char, [')', ']', '}', '>'])) {
                if (empty($stack) || array_pop($stack) !== $matchingBrackets[$char]) {
                    // If it doesn't match, add the score for this corrupted line
                    $totalScore += $scoreMap[$char];
                    $isCorrupted = true;
                    break; // Stop processing this line once corrupted
                }
            }
        }
    }

    return $totalScore;
}

// Calculate the total syntax error score
$result = calculateSyntaxErrorScore($inputFile);

echo "The total syntax error score is: $result\n";


//--- Part Two ---
function calculateAutocompleteScore($filename) {
    // Read the input file into an array of lines
    $lines = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

    // Define a mapping of closing characters to opening characters
    $matchingBrackets = [
        ')' => '(',
        ']' => '[',
        '}' => '{',
        '>' => '<'
    ];

    // Define the score for each closing character
    $scoreMap = [
        ')' => 1,
        ']' => 2,
        '}' => 3,
        '>' => 4
    ];

    // Array to store the autocomplete scores
    $autocompleteScores = [];

    // Process each line
    foreach ($lines as $line) {
        $stack = [];
        $isCorrupted = false;

        // Traverse each character in the line
        foreach (str_split($line) as $char) {
            // If it's an opening bracket, push to the stack
            if (in_array($char, ['(', '[', '{', '<'])) {
                $stack[] = $char;
            }
            // If it's a closing bracket, check if it matches the top of the stack
            elseif (in_array($char, [')', ']', '}', '>'])) {
                // Check if it matches the expected opening bracket
                if (empty($stack) || array_pop($stack) !== $matchingBrackets[$char]) {
                    // If it's corrupted, stop processing this line
                    $isCorrupted = true;
                    break;
                }
            }
        }

        // If the line is not corrupted, it is incomplete
        if (!$isCorrupted) {
            // Now, we need to generate the completion string
            $completionString = '';
            while ($bracket = array_pop($stack)) {
                // For each opening bracket, find the corresponding closing bracket
                $completionString .= array_search($bracket, $matchingBrackets);
            }

            // Calculate the score for the completion string
            $score = 0;
            foreach (str_split($completionString) as $char) {
                $score = $score * 5 + $scoreMap[$char];
            }

            // Add the score to the list
            $autocompleteScores[] = $score;
        }
    }

    // Sort the scores and find the middle score
    sort($autocompleteScores);
    $middleIndex = floor(count($autocompleteScores) / 2);
    return $autocompleteScores[$middleIndex];
}

// Calculate the middle autocomplete score
$result = calculateAutocompleteScore($inputFile);

echo "The middle autocomplete score is: $result\n";
