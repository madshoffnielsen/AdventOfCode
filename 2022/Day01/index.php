<?php

$elves = [];
$id = 0;

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        if ($line == PHP_EOL) {
            $id++;
        }
        else {
            if (!isset($elves[$id])) {
                $elves[$id] = 0;
            }

            $elves[$id] += intval($line);
        }
    }

    rsort($elves);

    echo 'MAX: ' . $elves[0] . PHP_EOL;

    $top3 = array_slice($elves, 0, 3);
    $tops = 0;

    foreach ($top3 as $top) {
        $tops += $top;
    }

    echo 'TOP 3: ' . $tops . PHP_EOL;
}