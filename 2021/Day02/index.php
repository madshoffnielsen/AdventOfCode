<?php
// File path
$filename = 'input.txt';

//--- Day 2: Dive! ---

// Function to process the course and calculate the final horizontal position and depth
function calculateSubmarinePosition($filename) {
    if (!file_exists($filename)) {
        return "Error: File not found.";
    }

    // Read the file and get the commands
    $commands = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $horizontal = 0;
    $depth = 0;

    // Loop through the commands and update the position and depth
    foreach ($commands as $command) {
        // Split the command into action and value
        list($action, $value) = explode(' ', $command);
        $value = (int)$value; // Convert value to an integer

        switch ($action) {
            case 'forward':
                $horizontal += $value;
                break;
            case 'down':
                $depth += $value;
                break;
            case 'up':
                $depth -= $value;
                break;
        }
    }

    // Multiply horizontal position by depth and return the result
    return $horizontal * $depth;
}

// Calculate and display the result
$result = calculateSubmarinePosition($filename);
echo "Final result (horizontal position * depth): $result\n";

//--- Part Two ---

// Function to process the course with aim and calculate the final horizontal position and depth
function calculateSubmarinePositionWithAim($filename) {
    if (!file_exists($filename)) {
        return "Error: File not found.";
    }

    // Read the file and get the commands
    $commands = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $horizontal = 0;
    $depth = 0;
    $aim = 0;

    // Loop through the commands and update position, depth, and aim
    foreach ($commands as $command) {
        // Split the command into action and value
        list($action, $value) = explode(' ', $command);
        $value = (int)$value; // Convert value to an integer

        switch ($action) {
            case 'forward':
                $horizontal += $value;
                $depth += $aim * $value;  // Increase depth by aim * forward value
                break;
            case 'down':
                $aim += $value;  // Increase aim by down value
                break;
            case 'up':
                $aim -= $value;  // Decrease aim by up value
                break;
        }
    }

    // Multiply horizontal position by depth and return the result
    return $horizontal * $depth;
}

// Calculate and display the result
$result = calculateSubmarinePositionWithAim($filename);
echo "Final result (horizontal position * depth): $result\n";
