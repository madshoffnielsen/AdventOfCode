<?php

$total = 0;
$totalPart2 = 0;

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $dim = explode('x', trim($line));

        $sides = [];
        $sides[] = (2 * $dim[0] * $dim[1]);
        $sides[] = (2 * $dim[1] * $dim[2]);
        $sides[] = (2 * $dim[2] * $dim[0]);

        $total += array_sum($sides) + (min($sides) / 2);

        // Part 2

        sort($dim);
        $totalPart2 += (2 * $dim[0]) + (2 * $dim[1]) + array_product($dim);
    }

    echo 'Total square foot: ' . $total . PHP_EOL;
    echo 'Total ribbon foot: ' . $totalPart2 . PHP_EOL;
}