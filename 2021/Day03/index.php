<?php
// File path
$inputFile = 'input.txt';

//--- Day 3: Binary Diagnostic ---

// Function to calculate the power consumption based on the diagnostic report
function calculatePowerConsumption($inputFile) {
    // Read the file and get the binary numbers
    $binaryNumbers = file($inputFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $bitLength = strlen($binaryNumbers[0]);  // Length of each binary number

    // Initialize counters for each bit position
    $bitCounts = array_fill(0, $bitLength, 0);

    // Count the number of 1s in each bit position
    foreach ($binaryNumbers as $number) {
        for ($i = 0; $i < $bitLength; $i++) {
            if ($number[$i] === '1') {
                $bitCounts[$i]++;
            }
        }
    }

    // Initialize gamma and epsilon rates as empty strings
    $gammaRate = '';
    $epsilonRate = '';

    // Calculate gamma and epsilon rates
    $totalNumbers = count($binaryNumbers);
    foreach ($bitCounts as $count) {
        if ($count > $totalNumbers / 2) {
            $gammaRate .= '1';
            $epsilonRate .= '0';
        } else {
            $gammaRate .= '0';
            $epsilonRate .= '1';
        }
    }

    // Convert gamma and epsilon rates to decimal
    $gammaRateDecimal = bindec($gammaRate);
    $epsilonRateDecimal = bindec($epsilonRate);

    // Calculate and return the power consumption
    return $gammaRateDecimal * $epsilonRateDecimal;
}

// Calculate and display the result
$result = calculatePowerConsumption($inputFile);
echo "Power consumption: $result\n";

//--- Part Two ---

// Function to calculate the life support rating
function calculateLifeSupportRating($inputFile) {
    // Read the file and get the binary numbers
    $binaryNumbers = file($inputFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

    // Function to find rating based on the given criteria
    function findRating($numbers, $criteria) {
        $bitLength = strlen($numbers[0]);

        for ($i = 0; $i < $bitLength; $i++) {
            // Count the occurrences of 0's and 1's at the i-th bit position
            $count0 = $count1 = 0;
            foreach ($numbers as $number) {
                if ($number[$i] === '0') {
                    $count0++;
                } else {
                    $count1++;
                }
            }

            // Determine the most or least common bit based on the criteria
            $keepBit = '';
            if ($criteria === 'oxygen') {
                // For oxygen, keep the most common bit (if equal, keep 1)
                $keepBit = ($count1 >= $count0) ? '1' : '0';
            } else {
                // For CO2 scrubber, keep the least common bit (if equal, keep 0)
                $keepBit = ($count0 <= $count1) ? '0' : '1';
            }

            // Filter the numbers based on the selected bit
            $numbers = array_filter($numbers, function($number) use ($i, $keepBit) {
                return $number[$i] === $keepBit;
            });

            // If only one number is left, break out of the loop
            if (count($numbers) === 1) {
                break;
            }
        }

        // Return the remaining number
        return array_values($numbers)[0];
    }

    // Find oxygen generator rating (criteria 'oxygen')
    $oxygenRatingBinary = findRating($binaryNumbers, 'oxygen');
    $oxygenRatingDecimal = bindec($oxygenRatingBinary);

    // Find CO2 scrubber rating (criteria 'co2')
    $co2RatingBinary = findRating($binaryNumbers, 'co2');
    $co2RatingDecimal = bindec($co2RatingBinary);

    // Calculate the life support rating
    return $oxygenRatingDecimal * $co2RatingDecimal;
}

// Calculate and display the result
$result = calculateLifeSupportRating($inputFile);
echo "Life support rating: $result\n";
