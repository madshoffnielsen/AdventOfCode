<?php
// File path
$inputFile = 'input.txt';

//--- Day 7: Handy Haversacks ---
// Read the input file
$input = file('input.txt', FILE_IGNORE_NEW_LINES);

// Parse the rules into a structured array
$rules = [];
foreach ($input as $line) {
    // Parse the main bag and its contents
    preg_match('/^(.+?) bags contain (.+)\.$/', $line, $matches);
    $bag = $matches[1];
    $contents = $matches[2];

    if ($contents === 'no other bags') {
        $rules[$bag] = [];
    } else {
        $contentsArray = explode(', ', $contents);
        foreach ($contentsArray as $content) {
            preg_match('/^(\d+) (.+?) bags?$/', $content, $contentMatches);
            $rules[$bag][$contentMatches[2]] = (int)$contentMatches[1];
        }
    }
}

// Part 1: Find all bags that can eventually contain "shiny gold"
function canContainShinyGold($bag, $rules) {
    if (!isset($rules[$bag])) return false;
    foreach ($rules[$bag] as $innerBag => $count) {
        if ($innerBag === 'shiny gold' || canContainShinyGold($innerBag, $rules)) {
            return true;
        }
    }
    return false;
}

$part1 = 0;
foreach ($rules as $bag => $contents) {
    if (canContainShinyGold($bag, $rules)) {
        $part1++;
    }
}

echo "Part 1: Bags that can contain 'shiny gold': $part1\n";


//--- Part Two ---
// Part 2: Count the total number of bags inside a "shiny gold" bag
function countBagsInside($bag, $rules) {
    if (!isset($rules[$bag])) return 0;
    $total = 0;
    foreach ($rules[$bag] as $innerBag => $count) {
        $total += $count + $count * countBagsInside($innerBag, $rules);
    }
    return $total;
}

$part2 = countBagsInside('shiny gold', $rules);

echo "Part 2: Bags required inside 'shiny gold': $part2\n";
