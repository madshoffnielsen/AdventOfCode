<?php

$totalScore = 0;
$totalScorePart2 = 0;

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $elf = explode(',', $line);
        $elf1 = explode('-', $elf[0]);
        $elf2 = explode('-', $elf[1]);

        if (($elf1[0] <= $elf2[0] && $elf1[1] >= $elf2[1]) ||
        $elf2[0] <= $elf1[0] && $elf2[1] >= $elf1[1]) {
            $totalScore += 1;
        }

        if (($elf1[0] <= $elf2[0] && $elf1[1] >= $elf2[1]) ||
            ($elf2[0] <= $elf1[0] && $elf2[1] >= $elf1[1]) ||
            ($elf1[0] >= $elf2[0] && $elf1[0] <= $elf2[1]) ||
            ($elf1[1] >= $elf2[0] && $elf1[1] <= $elf2[1]) ||
            ($elf2[0] >= $elf1[0] && $elf2[0] <= $elf1[1]) ||
            ($elf2[1] >= $elf1[0] && $elf2[1] <= $elf1[1])) {
            $totalScorePart2 += 1;
        }
    }

    echo 'Total score: ' . $totalScore . PHP_EOL;
    echo 'Total score part 2: ' . $totalScorePart2 . PHP_EOL;
}