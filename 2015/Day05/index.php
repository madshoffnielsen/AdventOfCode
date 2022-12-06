<?php

$total = 0;
$disallowed = ['ab', 'cd', 'pq', 'xy'];
$vowels = ['a', 'e', 'i', 'o', 'u'];

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        foreach ($disallowed as $badValue) {
            if (str_contains($line, $badValue)) {
                continue 2;
            }
        }

        $letters = str_split($line);
        $previous = '';

        $double = false;
        $countVowels = 0;
        foreach($letters as $letter) {
            if($letter == $previous) {
                $double = true;
            }

            if (in_array($letter, $vowels)) {
                $countVowels++;
            }

            $previous = $letter;
        }

        if ($double && $countVowels >= 3) {
            $total++;
        }
    }

    echo 'Total nice strings: ' . $total . PHP_EOL;
}