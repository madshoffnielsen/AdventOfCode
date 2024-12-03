<?php
// File path
$inputFile = 'input.txt';
$input = trim(file_get_contents($inputFile));
$initialTimers = array_map('intval', explode(',', $input));

//--- Day 6: Lanternfish ---
function simulateLanternfish($initialTimers, $days) {
    // Initialize an array to count fish at each timer value (0 to 8)
    $fishTimers = array_fill(0, 9, 0);
    
    // Populate the initial fish timer counts
    foreach ($initialTimers as $timer) {
        $fishTimers[$timer]++;
    }
    
    // Simulate the lanternfish lifecycle for the given number of days
    for ($day = 0; $day < $days; $day++) {
        $newFish = $fishTimers[0]; // Fish ready to spawn
        
        // Shift all other timers down by one
        for ($i = 0; $i < 8; $i++) {
            $fishTimers[$i] = $fishTimers[$i + 1];
        }
        
        // Reset the fish at timer 0 to timer 6 and add new fish at timer 8
        $fishTimers[6] += $newFish;
        $fishTimers[8] = $newFish;
    }
    
    // Sum all fish counts to get the total number of lanternfish
    return array_sum($fishTimers);
}

// Simulate for 80 days
$result = simulateLanternfish($initialTimers, 80);
echo "After 80 days, there are $result lanternfish.\n";

//--- Part Two ---

// Simulate for 256 days
$result = simulateLanternfish($initialTimers, 256);
echo "After 256 days, there are $result lanternfish.\n";
