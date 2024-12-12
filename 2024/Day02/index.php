<?php

function isSafeReport($levels) {
    $isIncreasing = true;
    $isDecreasing = true;

    // Loop through the levels to check the conditions
    for ($i = 0; $i < count($levels) - 1; $i++) {
        $difference = $levels[$i + 1] - $levels[$i];

        // Check if the difference is between 1 and 3
        if (abs($difference) < 1 || abs($difference) > 3) {
            return false;
        }

        // Determine if the report is consistently increasing or decreasing
        if ($difference < 0) {
            $isIncreasing = false;
        } elseif ($difference > 0) {
            $isDecreasing = false;
        }
    }

    // A report is safe if it is either strictly increasing or strictly decreasing
    return $isIncreasing || $isDecreasing;
}

function countSafeReports($filename) {
    $safeCount = 0;

    // Open the file and process each report
    if (($handle = fopen($filename, "r")) !== false) {
        while (($line = fgets($handle)) !== false) {
            // Parse the line into an array of integers
            $levels = array_map('intval', preg_split('/\s+/', trim($line)));

            // Check if the report is safe
            if (isSafeReport($levels)) {
                $safeCount++;
            }
        }
        fclose($handle);
    }

    return $safeCount;
}

// File path
$filename = "input.txt";

// Count and print the number of safe reports
$safeReports = countSafeReports($filename);
echo "Number of Safe Reports: " . $safeReports . PHP_EOL;

function isSafeWithDampener($levels) {
    // Check if the report is already safe
    if (isSafeReport($levels)) {
        return true;
    }

    // Attempt to remove each level one at a time
    for ($i = 0; $i < count($levels); $i++) {
        $modifiedLevels = $levels;
        unset($modifiedLevels[$i]); // Remove the current level
        $modifiedLevels = array_values($modifiedLevels); // Reindex the array

        // Check if the modified report is safe
        if (isSafeReport($modifiedLevels)) {
            return true;
        }
    }

    // If no single removal makes the report safe, it's unsafe
    return false;
}

function countSafeReportsWithDampener($filename) {
    $safeCount = 0;

    // Open the file and process each report
    if (($handle = fopen($filename, "r")) !== false) {
        while (($line = fgets($handle)) !== false) {
            // Parse the line into an array of integers
            $levels = array_map('intval', preg_split('/\s+/', trim($line)));

            // Check if the report is safe with the dampener
            if (isSafeWithDampener($levels)) {
                $safeCount++;
            }
        }
        fclose($handle);
    }

    return $safeCount;
}

// File path
$filename = "input.txt";

// Count and print the number of safe reports with the Problem Dampener
$safeReports = countSafeReportsWithDampener($filename);
echo "Number of Safe Reports (with Dampener): " . $safeReports . PHP_EOL;
