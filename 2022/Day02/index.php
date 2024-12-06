<?php

$totalScore = 0;
$totalScorePart2 = 0;

$score = [
    'A' => 1,
    'B' => 2,
    'C' => 3,
    'X' => 1,
    'Y' => 2,
    'Z' => 3,
];

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $line = trim($line);
        $play = explode(' ', $line);

        $totalScore += $score[$play[1]];

        // Win
        if ($line == 'C X' || $line == 'A Y' || $line == 'B Z') {
            $totalScore += 6;
        }

        // Draw
        if ($line == 'A X' || $line == 'B Y' || $line == 'C Z') {
            $totalScore += 3;
        }

        // Draw part 2
        if ($play[1] == 'Y') {
            $totalScorePart2 += 3;
            $totalScorePart2 += $score[$play[0]];
        }

        // Lose part 2
        if ($line == 'A X') {
            $totalScorePart2 += $score['Z'];
        }
        if ($line == 'B X') {
            $totalScorePart2 += $score['X'];
        }
        if ($line == 'C X') {
            $totalScorePart2 += $score['Y'];
        }

        // Win part 2
        if ($play[1] == 'Z') {
            $totalScorePart2 += 6;
            if ($line == 'A Z') {
                $totalScorePart2 += $score['Y'];
            }
            if ($line == 'B Z') {
                $totalScorePart2 += $score['Z'];
            }
            if ($line == 'C Z') {
                $totalScorePart2 += $score['X'];
            }
        }
    }

    echo 'Total score: ' . $totalScore . PHP_EOL;
    echo 'Total score part 2: ' . $totalScorePart2 . PHP_EOL;
}