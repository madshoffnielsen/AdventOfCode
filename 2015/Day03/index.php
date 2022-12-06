<?php

$total = 1;

$position = [0, 0];
$positionRobot = [0, 0];
$visited = [[]];

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $directions = str_split($line, 1);

        $visited[0][0] = true;

        foreach ($directions as $key => $direction) {
            if ($key % 2 != 0) {
                switch ($direction) {
                    case '>':
                        $position[0] += 1;
                        break;
                    case '<':
                        $position[0] -= 1;
                        break;
                    case '^':
                        $position[1] += 1;
                        break;
                    case 'v':
                        $position[1] -= 1;
                        break;
                }

                if (!isset($visited[$position[0]][$position[1]])) {
                    $visited[$position[0]][$position[1]] = true;
                    $total += 1;
                }
            }
            else {
                switch ($direction) {
                    case '>':
                        $positionRobot[0] += 1;
                        break;
                    case '<':
                        $positionRobot[0] -= 1;
                        break;
                    case '^':
                        $positionRobot[1] += 1;
                        break;
                    case 'v':
                        $positionRobot[1] -= 1;
                        break;
                }

                if (!isset($visited[$positionRobot[0]][$positionRobot[1]])) {
                    $visited[$positionRobot[0]][$positionRobot[1]] = true;
                    $total += 1;
                }
            }
        }
    }

    echo 'Total houses: ' . $total . PHP_EOL;
}