<?php

function readInputFromFile($filename) {
    $leftList = [];
    $rightList = [];

    // Open the file and read line by line
    if (($handle = fopen($filename, "r")) !== false) {
        while (($line = fgets($handle)) !== false) {
            // Split each line by whitespace to get the two columns
            $numbers = preg_split('/\s+/', trim($line));

            // Append numbers to the respective lists
            if (count($numbers) == 2) {
                $leftList[] = (int)$numbers[0];
                $rightList[] = (int)$numbers[1];
            }
        }
        fclose($handle);
    }

    return [$leftList, $rightList];
}

function calculateTotalDistance($leftList, $rightList) {
    // Sort both lists in ascending order
    sort($leftList);
    sort($rightList);

    $totalDistance = 0;

    // Calculate the total distance by pairing corresponding elements
    for ($i = 0; $i < count($leftList); $i++) {
        $totalDistance += abs($leftList[$i] - $rightList[$i]);
    }

    return $totalDistance;
}

// File path
$filename = "input.txt";

// Read lists from file
list($leftList, $rightList) = readInputFromFile($filename);

// Calculate and print the total distance
$totalDistance = calculateTotalDistance($leftList, $rightList);
echo "Total Distance: " . $totalDistance . PHP_EOL;



function calculateSimilarityScore($leftList, $rightList) {
    // Count occurrences of each number in the right list
    $rightCounts = array_count_values($rightList);

    $similarityScore = 0;

    // Calculate the similarity score based on occurrences in the right list
    foreach ($leftList as $number) {
        if (isset($rightCounts[$number])) {
            $similarityScore += $number * $rightCounts[$number];
        }
    }

    return $similarityScore;
}

// File path
$filename = "input.txt";

// Read lists from file
list($leftList, $rightList) = readInputFromFile($filename);

// Part Two: Calculate the similarity score
$similarityScore = calculateSimilarityScore($leftList, $rightList);
echo "Similarity Score: " . $similarityScore . PHP_EOL;

?>
