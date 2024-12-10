<?php
// File path
$inputFile = 'input.txt';

//--- Day 6: Custom Customs ---
// Read the input file
$input = file_get_contents('input.txt');

// Normalize line endings to Unix format (LF only)
$input = str_replace("\r\n", "\n", $input);

// Split the input into groups using "\n\n"
$groups = explode("\n\n", $input);

// Function to count unique "yes" answers in a group
function countUniqueYesAnswers($group) {
    // Remove newlines, then find unique characters
    $answers = str_replace("\n", '', $group);
    return count(array_unique(str_split($answers)));
}

// Calculate the total sum of unique "yes" answers for all groups
$total = 0;
foreach ($groups as $group) {
    $total += countUniqueYesAnswers(trim($group));
}

echo "Part 1: Unique: $total\n";


//--- Part Two ---
// Function to count common "yes" answers in a group
function countCommonYesAnswers($group) {
    // Split the group into individual people's answers
    $people = explode("\n", trim($group));
    // Convert each person's answers into a set of characters
    $commonAnswers = str_split($people[0]);
    foreach ($people as $person) {
        $commonAnswers = array_intersect($commonAnswers, str_split($person));
    }
    return count($commonAnswers);
}

// Calculate the total sum of common "yes" answers for all groups
$total = 0;
foreach ($groups as $group) {
    $total += countCommonYesAnswers($group);
}

echo "Part 2: Common: $total\n";