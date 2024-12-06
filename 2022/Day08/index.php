<?php

$grid = [[]];

$totalScore = 0;
$totalScorePart2 = 0;

$cols = 0;
$rows = 0;

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $trees = str_split(trim($line));
        $grid[$rows] = $trees;
        $rows++;
    }

    $cols = count($grid);
    $totalScore += (2 * $cols) + (2 * ($rows - 2));

    for ($x=1; $x < $cols-1; $x++) {
        $col = array_column($grid, $x);

        for ($y=1; $y < $rows-1; $y++) {
            $row = $grid[$y];

            $totalScore += checkVisibility($x, $y, $row, $col);
        }
    }

    for ($x=0; $x < $cols; $x++) {
        $col = array_column($grid, $x);
        for ($y=0; $y < $rows; $y++) {
            $row = $grid[$y];

            $score = checkScenicScore($x, $y, $row, $col);

            if ($score > $totalScorePart2) {
                $totalScorePart2 = $score;
            }
        }
    }

    echo 'Total visible trees: ' . $totalScore . PHP_EOL;
    echo 'Max scenic score: ' . $totalScorePart2 . PHP_EOL;
}

function checkVisibility($x, $y, $row, $col) {
    $return = 0;

    $xl = max(array_slice($row, 0, $x));
    $xr = max(array_slice($row, $x+1));
    $xt = max(array_slice($col, 0, $y));
    $xb = max(array_slice($col, $y+1));

    if ($xl < $row[$x] || $xr < $row[$x] || $xt < $row[$x] || $xb < $row[$x]) {
        $return = 1;
    }

    return $return;
}

function checkScenicScore($x, $y, $row, $col) {
    $currentTree = $row[$x];

    $xl = 0;
    $xr = 0;
    $xt = 0;
    $xb = 0;

    for ($i=$x-1; $i >= 0; $i--) {
        $xl++;

        if ($row[$i] >=$currentTree) {
            break;
        }
    }

    for ($i=$x+1; $i < count($row); $i++) {
        $xr++;

        if ($row[$i] >=$currentTree) {
            break;
        }
    }

    for ($i=$y-1; $i >= 0; $i--) {
        $xt++;

        if ($col[$i] >=$currentTree) {
            break;
        }
    }

    for ($i=$y+1; $i < count($col); $i++) {
        $xb++;

        if ($col[$i] >=$currentTree) {
            break;
        }
    }

    return $xl * $xr * $xt * $xb;
}