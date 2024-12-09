<?php
// File path
$inputFile = 'input.txt';

//--- Day 5: Binary Boarding ---
// Read input file
$input = file('input.txt', FILE_IGNORE_NEW_LINES);

// Function to decode a seat code to its row and column
function decodeSeat($code) {
    $binary = strtr($code, [
        'F' => '0',
        'B' => '1',
        'L' => '0',
        'R' => '1',
    ]);
    $row = bindec(substr($binary, 0, 7));
    $col = bindec(substr($binary, 7, 3));
    return [$row, $col];
}

// Part 1: Find the highest seat ID
$maxSeatID = 0;
$seatIDs = [];

foreach ($input as $seatCode) {
    [$row, $col] = decodeSeat($seatCode);
    $seatID = ($row * 8) + $col;
    $seatIDs[] = $seatID;
    $maxSeatID = max($maxSeatID, $seatID);
}

echo "Part 1: Highest seat ID: $maxSeatID\n";


//--- Part Two ---
// Part 2: Find the missing seat ID
sort($seatIDs); // Sort seat IDs
for ($i = 1; $i < count($seatIDs); $i++) {
    if ($seatIDs[$i] - $seatIDs[$i - 1] > 1) {
        $missingSeatID = $seatIDs[$i] - 1;
        break;
    }
}

echo "Part 2: Your seat ID: $missingSeatID\n";
