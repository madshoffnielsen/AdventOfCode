<?php
// File path
$inputFile = 'input.txt';

//--- Day 13: Shuttle Search ---
// Read the input file
$input = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$earliestTime = intval($input[0]);
$busOffsets = array_map(function ($value, $index) {
    return [
        'bus_id' => $value === 'x' ? null : intval($value),
        'offset' => $index
    ];
}, explode(',', $input[1]), array_keys(explode(',', $input[1])));

// Part 1: Find the earliest bus you can catch
function findEarliestBus($earliestTime, $busOffsets) {
    $minWait = PHP_INT_MAX;
    $bestBusId = null;

    foreach ($busOffsets as $offset) {
        $bus_id = $offset['bus_id'];
        if ($bus_id) {
            $waitTime = $bus_id - ($earliestTime % $bus_id);
            if ($waitTime < $minWait) {
                $minWait = $waitTime;
                $bestBusId = $bus_id;
            }
        }
    }

    return $bestBusId * $minWait;
}

$part1 = findEarliestBus($earliestTime, $busOffsets);
echo "Part 1: Earliest bus ID multiplied by wait time: $part1\n";


//--- Part Two ---
// Part 2: Find the earliest timestamp that satisfies all bus offsets
function findEarliestTimestamp($busOffsets) {
    $timestamp = 0;
    $step = 1;

    foreach ($busOffsets as $offset) {
        $bus_id = $offset['bus_id'];
        $desiredOffset = $offset['offset'];

        if (!$bus_id) {
            continue; // Skip if it's a placeholder 'x'
        }

        // Align the timestamp to match the bus's offset condition
        while (($timestamp + $desiredOffset) % $bus_id !== 0) {
            $timestamp += $step;
        }

        // Update step size to keep alignment with all previous buses
        $step *= $bus_id;
    }

    return $timestamp;
}

$part2 = findEarliestTimestamp($busOffsets);
echo "Part 2: Earliest timestamp: $part2\n";
