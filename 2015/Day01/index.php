<?php

$floor = 0;
$firstBasement = false;

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $length = strlen($line);

        for ($index = 0; $index < $length; $index++) {
            $floor += ($line[$index] == '(') ? 1 : -1;

            if ($floor == -1 && !$firstBasement) {
                echo 'First basement: ' . ($index + 1) . PHP_EOL;
                $firstBasement = true;
            }
        }
    }

    echo 'Final floor: ' . $floor;
}