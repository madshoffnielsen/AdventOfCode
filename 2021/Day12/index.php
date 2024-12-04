<?php
// File path
$inputFile = 'input.txt';

//--- Day 12: Passage Pathing ---
function parseInput($filePath) {
    // Read the input file and parse the connections
    $lines = file($filePath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $graph = [];
    foreach ($lines as $line) {
        [$from, $to] = explode('-', trim($line));
        $graph[$from][] = $to;
        $graph[$to][] = $from; // Undirected graph
    }
    return $graph;
}

function isSmallCave($cave) {
    return ctype_lower($cave);
}

function countPaths($graph, $current, $visited, $path) {
    if ($current === 'end') {
        return 1; // Reached the destination
    }

    if (isSmallCave($current)) {
        if (in_array($current, $visited)) {
            return 0; // Small cave already visited
        }
        $visited[] = $current;
    }

    $pathCount = 0;
    foreach ($graph[$current] as $neighbor) {
        if ($neighbor !== 'start') { // Never revisit the "start" cave
            $pathCount += countPaths($graph, $neighbor, $visited, $path);
        }
    }

    return $pathCount;
}

// Main program
$graph = parseInput($inputFile);
$totalPaths = countPaths($graph, 'start', [], []);

echo "Total paths: $totalPaths\n";


//--- Part Two ---
function countPaths2($graph, $current, $visited, $smallCaveVisitedTwice) {
    if ($current === 'end') {
        return 1; // Reached the destination
    }

    if (isSmallCave($current)) {
        if (isset($visited[$current])) {
            if ($visited[$current] === 1 && !$smallCaveVisitedTwice) {
                $smallCaveVisitedTwice = true; // Allow one small cave to be visited twice
            } else {
                return 0; // Small cave already visited twice
            }
        }
        $visited[$current] = ($visited[$current] ?? 0) + 1;
    }

    $pathCount = 0;
    foreach ($graph[$current] as $neighbor) {
        if ($neighbor !== 'start') { // Never revisit the "start" cave
            $pathCount += countPaths2($graph, $neighbor, $visited, $smallCaveVisitedTwice);
        }
    }

    // Backtrack to allow other paths to use the current cave correctly
    if (isSmallCave($current)) {
        $visited[$current]--;
        if ($visited[$current] === 0) {
            unset($visited[$current]);
        }
    }

    return $pathCount;
}

// Main program
$graph = parseInput($inputFile);
$totalPaths = countPaths2($graph, 'start', [], false);

echo "Total paths: $totalPaths\n";