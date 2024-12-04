<?php
// File path
$inputFile = 'input.txt';

//--- Day 17: Trick Shot ---
// Function to read the input file and extract the target area
function readInputFromFile($filename) {
    $fileContent = file_get_contents($filename);
    
    // Extract target area using regular expression
    preg_match('/x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)/', $fileContent, $matches);
    
    if (count($matches) === 5) {
        $xMin = (int) $matches[1];
        $xMax = (int) $matches[2];
        $yMin = (int) $matches[3];
        $yMax = (int) $matches[4];
        
        return [$xMin, $xMax, $yMin, $yMax];
    } else {
        throw new Exception("Invalid input format.");
    }
}

// Function to simulate the trajectory of the probe
function simulateTrajectory($vx, $vy, $xMin, $xMax, $yMin, $yMax) {
    $x = 0;
    $y = 0;
    $maxY = 0;
    
    while ($x <= $xMax && $y >= $yMin) {
        // Update positions
        $x += $vx;
        $y += $vy;
        
        // Track maximum Y position
        $maxY = max($maxY, $y);
        
        // Check if the probe is within the target area
        if ($x >= $xMin && $x <= $xMax && $y >= $yMin && $y <= $yMax) {
            return $maxY;  // The probe landed inside the target area
        }
        
        // Update velocities
        if ($vx > 0) {
            $vx--;  // Drag decreases x velocity
        }
        $vy--;  // Gravity decreases y velocity
    }
    
    return null;  // The probe misses the target area
}

// Function to find the highest Y position
function findHighestYPosition($xMin, $xMax, $yMin, $yMax) {
    $maxHeight = 0;
    $validVelocities = 0;
    
    // Iterate over possible initial velocities
    for ($vx = 0; $vx <= $xMax; $vx++) {
        for ($vy = $yMin; $vy <= abs($yMin); $vy++) {
            $maxY = simulateTrajectory($vx, $vy, $xMin, $xMax, $yMin, $yMax);
            if ($maxY !== null) {
                $validVelocities++;
                $maxHeight = max($maxHeight, $maxY);
            }
        }
    }
    
    return $maxHeight;
}

// Read the target area from the input file
list($xMin, $xMax, $yMin, $yMax) = readInputFromFile($inputFile);

// Find the highest Y position the probe can reach
$highestY = findHighestYPosition($xMin, $xMax, $yMin, $yMax);

echo "The highest Y position reached is: " . $highestY . "\n";


//--- Part Two ---
// Function to simulate the trajectory of the probe
function simulateTrajectory2($vx, $vy, $xMin, $xMax, $yMin, $yMax) {
    $x = 0;
    $y = 0;
    
    while ($x <= $xMax && $y >= $yMin) {
        // Update positions
        $x += $vx;
        $y += $vy;
        
        // Check if the probe is within the target area
        if ($x >= $xMin && $x <= $xMax && $y >= $yMin && $y <= $yMax) {
            return true;  // The probe landed inside the target area
        }
        
        // Update velocities
        if ($vx > 0) {
            $vx--;  // Drag decreases x velocity
        }
        $vy--;  // Gravity decreases y velocity
    }
    
    return false;  // The probe misses the target area
}

// Function to find the total number of valid velocities
function findValidVelocities($xMin, $xMax, $yMin, $yMax) {
    $validVelocities = 0;
    
    // Iterate over possible initial velocities
    for ($vx = 0; $vx <= $xMax; $vx++) {
        for ($vy = $yMin; $vy <= abs($yMin); $vy++) {
            if (simulateTrajectory2($vx, $vy, $xMin, $xMax, $yMin, $yMax)) {
                $validVelocities++;
            }
        }
    }
    
    return $validVelocities;
}

// Read the target area from the input file
list($xMin, $xMax, $yMin, $yMax) = readInputFromFile($inputFile);

// Find the number of valid initial velocities
$validVelocities = findValidVelocities($xMin, $xMax, $yMin, $yMax);

echo "The number of valid initial velocities is: " . $validVelocities . "\n";
