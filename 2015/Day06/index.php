<?php

$total = 0;
$totalPart2 = 0;

$lights = array_fill(0, 1000, array_fill(0, 1000, false));
$lightsPart2 = array_fill(0, 1000, array_fill(0, 1000, 0));

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $args = explode(' ', $line);

        // Toggle
        if (count($args) == 4) {
            $from = explode(',', $args[1]);
            $to = explode(',', $args[3]);

            for ($x=$from[0]; $x <= $to[0]; $x++) {
                for ($y=$from[1]; $y <= $to[1]; $y++) {
                    $lights[$x][$y] = !$lights[$x][$y];
                    $lightsPart2[$x][$y] += 2;
                }
            }
        }
        else {
            $onOff = $args[1] == 'on' ? true : false;
            $from = explode(',', $args[2]);
            $to = explode(',', $args[4]);

            for ($x=$from[0]; $x <= $to[0]; $x++) {
                for ($y=$from[1]; $y <= $to[1]; $y++) {
                    $lights[$x][$y] = $onOff;

                    if ($onOff) {
                        $lightsPart2[$x][$y] += 1;
                    }
                    else {
                        if ($lightsPart2[$x][$y] >=1) {
                            $lightsPart2[$x][$y] -= 1;
                        }
                    }
                }
            }
        }

    }

    for ($i=0; $i < 1000; $i++) {
        for ($j=0; $j < 1000; $j++) {
            if ($lights[$i][$j]) {
                $total++;
            }
        }
        $totalPart2 += array_sum($lightsPart2[$i]);
    }

    echo 'Total lights on: ' . $total . PHP_EOL;
    echo 'Total lights on part 2: ' . $totalPart2 . PHP_EOL;
}