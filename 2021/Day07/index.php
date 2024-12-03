<?php
// File path
$filename = 'input.txt';

//--- Day 7: The Treachery of Whales ---
function calculateMinimumFuel($positions) {
    sort($positions); // Sort the positions
    $median = $positions[floor(count($positions) / 2)]; // Find the median
    
    // Calculate the total fuel cost to align at the median
    $totalFuel = 0;
    foreach ($positions as $pos) {
        $totalFuel += abs($pos - $median);
    }
    
    return $totalFuel;
}

$input = trim(file_get_contents($filename));
$positions = array_map('intval', explode(',', $input));

// Calculate the minimum fuel
$result = calculateMinimumFuel($positions);
echo "The minimum fuel required is $result.\n";


//--- Part Two ---
function calculateFuelCost($positions, $target) {
    $totalFuel = 0;
    foreach ($positions as $pos) {
        $distance = abs($pos - $target);
        $totalFuel += ($distance * ($distance + 1)) / 2; // Sum of first n natural numbers
    }
    return $totalFuel;
}

function findOptimalPosition($positions) {
    $minPos = min($positions);
    $maxPos = max($positions);
    $minFuel = PHP_INT_MAX;

    for ($target = $minPos; $target <= $maxPos; $target++) {
        $fuel = calculateFuelCost($positions, $target);
        if ($fuel < $minFuel) {
            $minFuel = $fuel;
        }
    }

    return $minFuel;
}

$input = trim(file_get_contents($filename));
$positions = array_map('intval', explode(',', $input));

// Find the minimum fuel required
$result = findOptimalPosition($positions);
echo "The minimum fuel required is $result.\n";
