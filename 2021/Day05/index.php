<?php
// File path
$filename = 'input.txt';

// Parse the input file
$vents = parseInput($filename);

//--- Day 5: Hydrothermal Venture ---
// Function to parse the input
function parseInput($filename) {
    $lines = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $vents = [];
    
    foreach ($lines as $line) {
        // Extract coordinates using regular expression
        preg_match('/(\d+),(\d+) -> (\d+),(\d+)/', $line, $matches);
        $vents[] = [
            'x1' => (int)$matches[1],
            'y1' => (int)$matches[2],
            'x2' => (int)$matches[3],
            'y2' => (int)$matches[4]
        ];
    }
    
    return $vents;
}

// Function to calculate the number of points with overlaps
function countOverlaps($vents) {
    // Create an empty grid (size 1000x1000 as it's enough for most input sizes)
    $grid = array_fill(0, 1000, array_fill(0, 1000, 0));
    
    // Mark the grid with vent lines
    foreach ($vents as $vent) {
        // If it's a horizontal line
        if ($vent['y1'] === $vent['y2']) {
            $x1 = min($vent['x1'], $vent['x2']);
            $x2 = max($vent['x1'], $vent['x2']);
            for ($x = $x1; $x <= $x2; $x++) {
                $grid[$vent['y1']][$x]++;
            }
        }
        // If it's a vertical line
        elseif ($vent['x1'] === $vent['x2']) {
            $y1 = min($vent['y1'], $vent['y2']);
            $y2 = max($vent['y1'], $vent['y2']);
            for ($y = $y1; $y <= $y2; $y++) {
                $grid[$y][$vent['x1']]++;
            }
        }
    }
    
    // Count the number of points where at least two lines overlap
    $overlapCount = 0;
    foreach ($grid as $row) {
        foreach ($row as $cell) {
            if ($cell >= 2) {
                $overlapCount++;
            }
        }
    }
    
    return $overlapCount;
}

// Output the result
$result = countOverlaps($vents);
echo "The number of points where at least two lines overlap is: $result\n";


//--- Part Two ---

// Function to calculate the number of points with overlaps, including diagonals
function countOverlaps2($vents) {
    // Create an empty grid (size 1000x1000 as it's enough for most input sizes)
    $grid = array_fill(0, 1000, array_fill(0, 1000, 0));
    
    // Mark the grid with vent lines
    foreach ($vents as $vent) {
        // If it's a horizontal line
        if ($vent['y1'] === $vent['y2']) {
            $x1 = min($vent['x1'], $vent['x2']);
            $x2 = max($vent['x1'], $vent['x2']);
            for ($x = $x1; $x <= $x2; $x++) {
                $grid[$vent['y1']][$x]++;
            }
        }
        // If it's a vertical line
        elseif ($vent['x1'] === $vent['x2']) {
            $y1 = min($vent['y1'], $vent['y2']);
            $y2 = max($vent['y1'], $vent['y2']);
            for ($y = $y1; $y <= $y2; $y++) {
                $grid[$y][$vent['x1']]++;
            }
        }
        // If it's a diagonal line (45-degree)
        else {
            $x1 = $vent['x1'];
            $y1 = $vent['y1'];
            $x2 = $vent['x2'];
            $y2 = $vent['y2'];

            // Determine direction of the diagonal (up-right, down-left, etc.)
            $xStep = $x2 > $x1 ? 1 : -1;
            $yStep = $y2 > $y1 ? 1 : -1;
            
            // Traverse along the diagonal and increment cells
            while ($x1 !== $x2 + $xStep && $y1 !== $y2 + $yStep) {
                $grid[$y1][$x1]++;
                $x1 += $xStep;
                $y1 += $yStep;
            }
        }
    }
    
    // Count the number of points where at least two lines overlap
    $overlapCount = 0;
    foreach ($grid as $row) {
        foreach ($row as $cell) {
            if ($cell >= 2) {
                $overlapCount++;
            }
        }
    }
    
    return $overlapCount;
}

// Output the result
$result = countOverlaps2($vents);
echo "The number of points where at least two lines overlap is: $result\n";
