<?php
// File path
$inputFile = 'input.txt';

//--- Day 8: Handheld Halting ---
// Read the input file
$input = file('input.txt', FILE_IGNORE_NEW_LINES);

// Parse the instructions
$instructions = [];
foreach ($input as $line) {
    [$operation, $argument] = explode(' ', $line);
    $instructions[] = ['operation' => $operation, 'argument' => (int)$argument];
}

// Function to execute the program
function executeProgram($instructions, &$accumulator) {
    $executed = [];
    $pointer = 0;
    $accumulator = 0;

    while ($pointer < count($instructions)) {
        // Check for infinite loop
        if (isset($executed[$pointer])) {
            return false;
        }
        $executed[$pointer] = true;

        // Fetch current instruction
        $operation = $instructions[$pointer]['operation'];
        $argument = $instructions[$pointer]['argument'];

        // Execute instruction
        switch ($operation) {
            case 'nop':
                $pointer++;
                break;
            case 'acc':
                $accumulator += $argument;
                $pointer++;
                break;
            case 'jmp':
                $pointer += $argument;
                break;
        }
    }

    return true;
}

// Part 1: Find accumulator value before infinite loop
$part1Accumulator = 0;
executeProgram($instructions, $part1Accumulator);
echo "Part 1: Accumulator before infinite loop: $part1Accumulator\n";


//--- Part Two ---
// Part 2: Fix the program and find accumulator value after termination
function fixProgram($instructions) {
    for ($i = 0; $i < count($instructions); $i++) {
        // Only change `nop` to `jmp` or `jmp` to `nop`
        if ($instructions[$i]['operation'] === 'nop') {
            $instructions[$i]['operation'] = 'jmp';
        } elseif ($instructions[$i]['operation'] === 'jmp') {
            $instructions[$i]['operation'] = 'nop';
        } else {
            continue;
        }

        // Try executing the program
        $accumulator = 0;
        if (executeProgram($instructions, $accumulator)) {
            return $accumulator;
        }

        // Revert the change
        $instructions[$i]['operation'] = $instructions[$i]['operation'] === 'nop' ? 'jmp' : 'nop';
    }

    return null;
}

$part2Accumulator = fixProgram($instructions);
echo "Part 2: Accumulator after program termination: $part2Accumulator\n";
