<?php

$totalScore = 0;
$totalScorePart2 = 0;

$group = [];
$groupIndex = 0;

$score = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $length = strlen(trim($line)) / 2;
        $string1 = array_unique(str_split(substr($line, 0, $length)));
        $string2 = array_unique(str_split(substr($line, $length)));

        foreach ($string1 as $char1) {
            if (in_array($char1, $string2)) {
                $totalScore += array_search($char1, $score, true);
            }
        }

        // Part 2
        $group[$groupIndex++] = array_unique(str_split(trim($line)));

        if ($groupIndex == 3) {
            $groupIndex = 0;
            foreach ($group[0] as $char1) {
                if (in_array($char1, $group[1]) && in_array($char1, $group[2])) {
                    $totalScorePart2 += array_search($char1, $score, true);
                }
            }
        }
    }

    echo 'Total score: ' . $totalScore . PHP_EOL;
    echo 'Total score part 2: ' . $totalScorePart2 . PHP_EOL;
}