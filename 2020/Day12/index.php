<?php
// File path
$inputFile = 'input.txt';

//--- Day 12: Rain Risk ---
// Read the input file
$input = file('input.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

// Part 1: Simulate ship movement
function simulateShip($instructions) {
    $x = 0; // East-West position
    $y = 0; // North-South position
    $direction = 90; // East (0=N, 90=E, 180=S, 270=W)

    foreach ($instructions as $instruction) {
        $action = $instruction[0];
        $value = (int)substr($instruction, 1);

        switch ($action) {
            case 'N': $y += $value; break;
            case 'S': $y -= $value; break;
            case 'E': $x += $value; break;
            case 'W': $x -= $value; break;
            case 'L': $direction = ($direction - $value + 360) % 360; break;
            case 'R': $direction = ($direction + $value) % 360; break;
            case 'F':
                if ($direction === 0) $y += $value;
                if ($direction === 90) $x += $value;
                if ($direction === 180) $y -= $value;
                if ($direction === 270) $x -= $value;
                break;
        }
    }

    return abs($x) + abs($y); // Manhattan distance
}

// Solve Part 1
$part1 = simulateShip($input);
echo "Part 1: Manhattan distance: $part1\n";


//--- Part Two ---
// Part 2: Simulate ship and waypoint movement
function simulateWaypoint($instructions) {
    $shipX = 0;
    $shipY = 0;
    $waypointX = 10; // Waypoint relative to ship
    $waypointY = 1;

    foreach ($instructions as $instruction) {
        $action = $instruction[0];
        $value = (int)substr($instruction, 1);

        switch ($action) {
            case 'N': $waypointY += $value; break;
            case 'S': $waypointY -= $value; break;
            case 'E': $waypointX += $value; break;
            case 'W': $waypointX -= $value; break;
            case 'L':
                for ($i = 0; $i < $value / 90; $i++) {
                    $temp = $waypointX;
                    $waypointX = -$waypointY;
                    $waypointY = $temp;
                }
                break;
            case 'R':
                for ($i = 0; $i < $value / 90; $i++) {
                    $temp = $waypointX;
                    $waypointX = $waypointY;
                    $waypointY = -$temp;
                }
                break;
            case 'F':
                $shipX += $waypointX * $value;
                $shipY += $waypointY * $value;
                break;
        }
    }

    return abs($shipX) + abs($shipY); // Manhattan distance
}

// Solve Part 2
$part2 = simulateWaypoint($input);
echo "Part 2: Manhattan distance: $part2\n";
