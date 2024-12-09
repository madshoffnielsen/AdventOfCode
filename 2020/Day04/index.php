<?php
// File path
$inputFile = 'input.txt';

//--- Day 4: Passport Processing ---
// Read input file and parse passports
$input = file_get_contents('input.txt');
$lines = explode("\n", $input);

$passports = [];
$passports[] = "";
$nbr_passports = 0;

foreach($lines as $line) {
    if (empty(trim($line))) {
        $nbr_passports++;
        $passports[] = "";
        continue;
    }

    $passports[$nbr_passports] .= " " . $line;
}

// Function to validate a passport for required fields (Part 1)
function hasRequiredFields($passport) {
    $requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];
    foreach ($requiredFields as $field) {
        if (!preg_match("/\b$field:/", $passport)) {
            return false;
        }
    }
    return true;
}

// Part 1: Count valid passports based on required fields
$validPart1 = 0;
foreach ($passports as $passport) {
    if (hasRequiredFields($passport)) {
        $validPart1++;
    }
}
echo "Part 1: Valid passports (required fields): $validPart1\n";


//--- Part Two ---
// Function to validate fields based on rules (Part 2)
function isValidPassport($passport) {
    $fields = [];
    preg_match_all('/(\w+):([^\s]+)/', $passport, $matches, PREG_SET_ORDER);
    foreach ($matches as $match) {
        $fields[$match[1]] = $match[2];
    }

    // Validate each field
    return isset($fields['byr']) && preg_match('/^\d{4}$/', $fields['byr']) && (int)$fields['byr'] >= 1920 && (int)$fields['byr'] <= 2002 &&
           isset($fields['iyr']) && preg_match('/^\d{4}$/', $fields['iyr']) && (int)$fields['iyr'] >= 2010 && (int)$fields['iyr'] <= 2020 &&
           isset($fields['eyr']) && preg_match('/^\d{4}$/', $fields['eyr']) && (int)$fields['eyr'] >= 2020 && (int)$fields['eyr'] <= 2030 &&
           isset($fields['hgt']) && preg_match('/^(\d+)(cm|in)$/', $fields['hgt'], $hgt) && (
               ($hgt[2] === 'cm' && (int)$hgt[1] >= 150 && (int)$hgt[1] <= 193) ||
               ($hgt[2] === 'in' && (int)$hgt[1] >= 59 && (int)$hgt[1] <= 76)
           ) &&
           isset($fields['hcl']) && preg_match('/^#[0-9a-f]{6}$/', $fields['hcl']) &&
           isset($fields['ecl']) && in_array($fields['ecl'], ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) &&
           isset($fields['pid']) && preg_match('/^\d{9}$/', $fields['pid']);
}

// Part 2: Count valid passports based on field validation rules
$validPart2 = 0;
foreach ($passports as $passport) {
    if (hasRequiredFields($passport) && isValidPassport($passport)) {
        $validPart2++;
    }
}
echo "Part 2: Valid passports (with validation rules): $validPart2\n";
