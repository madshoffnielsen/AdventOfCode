<?php

$totalScore = 0;
$totalScorePart2 = PHP_INT_MAX;

$folderSize = [];
$filesystem = [];

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $args = explode(' ', trim($line));

        // Change directory
        if ($args[0] == '$' && $args[1] == 'cd') {
            if ($args[2] == '..') {
                array_pop($filesystem);
            }
            else {
                if ($args[2] == '/') {
                    array_push($filesystem, 'root');
                }
                else {
                    array_push($filesystem, $args[2]);
                }
            }
        }

        // Count file size
        if (is_numeric($args[0])) {
            $depth = count($filesystem);

            for ($i=0; $i < $depth; $i++) {
                $depthPath = array_slice($filesystem, 0 , $i+1);
                $stringPath = implode('/', $depthPath);

                if (isset($folderSize[$stringPath])) {
                    $folderSize[$stringPath] += $args[0];
                }
                else {
                    $folderSize[$stringPath] = $args[0];
                }
            }
        }
    }

    $totalScore = array_sum(array_filter($folderSize, function($total) {
        return $total <= 100000;
    }));

    $diskSpace = 70000000;
    $updateSpace = 30000000;
    $usedSpace = $folderSize['root'];

    $freeSpace = $diskSpace - $usedSpace;
    $neededSpace = $updateSpace - $freeSpace;

    foreach ($folderSize as $path => $size) {
        if ($size >= $neededSpace && $size < $totalScorePart2) {
            $totalScorePart2 = $size;
        }
    }

    echo 'Part 1: ' . $totalScore . PHP_EOL;
    echo 'Part 2: ' . $totalScorePart2 . PHP_EOL;
}
