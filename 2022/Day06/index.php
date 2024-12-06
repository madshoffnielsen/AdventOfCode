<?php

$totalScore = '';
$totalScorePart2 = '';

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $length = strlen($line);
        $chars = str_split($line);

        for ($totalScore=3; $totalScore < $length; $totalScore++) {
            $unique = array_unique([
                $chars[$totalScore],
                $chars[$totalScore-1],
                $chars[$totalScore-2],
                $chars[$totalScore-3],
            ]);
            if (count($unique) == 4) {
                break;
            }
        }

        for ($totalScorePart2=14; $totalScorePart2 < $length; $totalScorePart2++) {
            $unique = array_unique([
                $chars[$totalScorePart2],
                $chars[$totalScorePart2-1],
                $chars[$totalScorePart2-2],
                $chars[$totalScorePart2-3],
                $chars[$totalScorePart2-4],
                $chars[$totalScorePart2-5],
                $chars[$totalScorePart2-6],
                $chars[$totalScorePart2-7],
                $chars[$totalScorePart2-8],
                $chars[$totalScorePart2-9],
                $chars[$totalScorePart2-10],
                $chars[$totalScorePart2-11],
                $chars[$totalScorePart2-12],
                $chars[$totalScorePart2-13]
            ]);
            if (count($unique) == 14) {
                break;
            }
        }
    }

    echo 'First marker: ' . $totalScore + 1 . PHP_EOL;
    echo 'Total score part 2: ' . $totalScorePart2 + 1 . PHP_EOL;
}