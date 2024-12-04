<?php
// File path
$inputFile = 'input.txt';

//--- Day 13: Transparent Origami ---
function parseInput($filePath) {
    $lines = file($filePath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $dots = [];
    $folds = [];

    foreach ($lines as $line) {
        if (strpos($line, "fold along") === 0) {
            preg_match("/fold along ([xy])=(\d+)/", $line, $matches);
            $folds[] = [$matches[1], (int)$matches[2]];
        } elseif (strpos($line, ',') !== false) {
            $dots[] = array_map('intval', explode(',', $line));
        }
    }

    return [$dots, $folds];
}

function foldPaper($dots, $fold) {
    [$axis, $line] = $fold;
    $newDots = [];

    foreach ($dots as [$x, $y]) {
        if ($axis === 'x' && $x > $line) {
            $x = $line - ($x - $line); // Reflect x-coordinate
        } elseif ($axis === 'y' && $y > $line) {
            $y = $line - ($y - $line); // Reflect y-coordinate
        }
        $newDots["$x,$y"] = [$x, $y]; // Use a map to ensure uniqueness
    }

    return array_values($newDots);
}

function countDotsAfterFirstFold($filePath) {
    [$dots, $folds] = parseInput($filePath);
    $dots = foldPaper($dots, $folds[0]); // Apply the first fold
    return count($dots);
}

// Main program
$result = countDotsAfterFirstFold($inputFile);
echo "Number of visible dots after the first fold: $result\n";


//--- Part Two ---
function applyAllFolds($dots, $folds) {
    foreach ($folds as $fold) {
        $dots = foldPaper($dots, $fold);
    }
    return $dots;
}

function visualizeDots($dots) {
    // Determine the size of the grid
    $maxX = $maxY = 0;
    foreach ($dots as [$x, $y]) {
        $maxX = max($maxX, $x);
        $maxY = max($maxY, $y);
    }

    // Create a blank grid
    $grid = array_fill(0, $maxY + 1, array_fill(0, $maxX + 1, ' '));

    // Mark the dots
    foreach ($dots as [$x, $y]) {
        $grid[$y][$x] = '#';
    }

    // Print the grid
    foreach ($grid as $line) {
        echo implode('', $line) . "\n";
    }
}

function getActivationCode($filePath) {
    [$dots, $folds] = parseInput($filePath);
    $dots = applyAllFolds($dots, $folds); // Apply all folds
    visualizeDots($dots); // Display the resulting grid
}

// Main program
getActivationCode($inputFile);
