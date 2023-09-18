<?php

function isNiceStringPart1($str) {
    // Check for at least three vowels.
    $vowelCount = preg_match_all('/[aeiou]/', $str);

    // Check for at least one letter that appears twice in a row.
    $hasDoubleLetter = preg_match('/([a-z])\\1/', $str);

    // Check for the disallowed substrings.
    $disallowedSubstrings = array('ab', 'cd', 'pq', 'xy');
    $containsDisallowed = false;
    foreach ($disallowedSubstrings as $substring) {
        if (strpos($str, $substring) !== false) {
            $containsDisallowed = true;
            break;
        }
    }

    // A string is nice if it meets all the criteria.
    return ($vowelCount >= 3 && $hasDoubleLetter && !$containsDisallowed);
}

// Read the text file line by line.
$filename = 'input.txt';
$niceCount = 0;

$file = fopen($filename, 'r');
if ($file) {
    while (($line = fgets($file)) !== false) {
        if (isNiceStringPart1(trim($line))) {
            $niceCount++;
        }
    }
    fclose($file);
}

echo "Number of nice strings part 1: " . $niceCount . "\n";

function isNiceStringPart2($str) {
    // Check for a pair of any two letters that appears at least twice in the string without overlapping.
    $pairPattern = '/(..).*\1/';

    // Check for a letter which repeats with exactly one letter between them.
    $repeatWithOneInBetween = '/(.).\1/';

    return (preg_match($pairPattern, $str) && preg_match($repeatWithOneInBetween, $str));
}

// Read the text file line by line.
$filename = 'input.txt';
$niceCount = 0;

$file = fopen($filename, 'r');
if ($file) {
    while (($line = fgets($file)) !== false) {
        if (isNiceStringPart2(trim($line))) {
            $niceCount++;
        }
    }
    fclose($file);
}

echo "Number of nice strings part 2: " . $niceCount;