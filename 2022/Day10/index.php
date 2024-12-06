<?php

$cyclesCheck = [20, 60, 100, 140, 180, 220];

$totalScore = 0;

$crt = [];
$cycle = 0;
$crtCount = 0;
$x = 1;

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $args = explode(' ', trim($line));

        if ($x-1 == $crtCount || $x == $crtCount || $x+1 == $crtCount) {
            $crt[$cycle] = '#';
        }
        else {
            $crt[$cycle] = ' ';
        }

        $cycle++;
        $crtCount++;

        if ($crtCount == 40) {
            $crtCount = 0;
        }

        if ($args[0] == 'noop') {
            if (in_array($cycle, $cyclesCheck)) {
                $totalScore += ($x * $cycle);
            }
        }
        else {
            if (in_array($cycle, $cyclesCheck)) {
                $totalScore += ($x * $cycle);
            }

            if ($x-1 == $crtCount || $x == $crtCount || $x+1 == $crtCount) {
                $crt[$cycle] = '#';
            }
            else {
                $crt[$cycle] = ' ';
            }

            $cycle++;
            $crtCount++;

            if ($crtCount == 40) {
                $crtCount = 0;
            }

            if (in_array($cycle, $cyclesCheck)) {
                $totalScore += ($x * $cycle);
            }

            $x += $args[1];
        }
    }

    echo 'Total signal: ' . $totalScore . PHP_EOL;

    echo implode('', array_slice($crt, 0, 40)) . PHP_EOL;
    echo implode('', array_slice($crt, 40, 40)) . PHP_EOL;
    echo implode('', array_slice($crt, 80, 40)) . PHP_EOL;
    echo implode('', array_slice($crt, 120, 40)) . PHP_EOL;
    echo implode('', array_slice($crt, 160, 40)) . PHP_EOL;
    echo implode('', array_slice($crt, 200, 40)) . PHP_EOL;
}
