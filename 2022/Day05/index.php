<?php

$totalScore = '';
$totalScorePart2 = '';

$ship = [0, 1 => [], 2 => [], 3 => [], 4 => [], 5 => [], 6 => [], 7 => [], 8 => [], 9 => []];
$shipPart2 = [0, 1 => [], 2 => [], 3 => [], 4 => [], 5 => [], 6 => [], 7 => [], 8 => [], 9 => []];

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $input = str_split($line, 4);

        if ($input[0] != 'move' && intval($input[0]) != 1) {
            foreach ($input as $key => $value) {
                if (!empty(trim($value))) {
                    $value = str_replace(['[',']'], '', trim($value));
                    if (!isset($ship[$key+1])){
                        $ship[$key+1][] = $value;
                        $shipPart2[$key+1][] = $value;
                    }
                    else {
                        array_push($ship[$key+1], $value);
                        array_push($shipPart2[$key+1], $value);
                    }
                }
            }
        }

        if ($input[0] == 'move') {
            $moveCmd = explode(' ', trim($line));
            $amount = $moveCmd[1];
            $from = $moveCmd[3];
            $to = $moveCmd[5];

            for ($index=0; $index < $amount; $index++) {
                $val = array_shift($ship[$from]);
                array_unshift($ship[$to], $val);
            }

            $crane = [];

            for ($index=0; $index < $amount; $index++) {
                $crane[] = array_shift($shipPart2[$from]);
            }
            foreach (array_reverse($crane) as $key => $val) {
                array_unshift($shipPart2[$to], $val);
            }
        }
    }

    foreach ($ship as $key => $value) {
        if (isset($value[0])) {
            $totalScore .= $value[0];
        }
    }

    foreach ($shipPart2 as $key => $value) {
        if (isset($value[0])) {
            $totalScorePart2 .= $value[0];
        }
    }

    echo 'Total score: ' . $totalScore . PHP_EOL;
    echo 'Total score part 2: ' . $totalScorePart2 . PHP_EOL;
}