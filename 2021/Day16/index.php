<?php
// File path
$inputFile = 'input.txt';

//--- Day 16: Packet Decoder ---
// Function to convert hex to binary
function hexToBin($hexStr) {
    $binStr = '';
    for ($i = 0; $i < strlen($hexStr); $i++) {
        $binStr .= str_pad(base_convert($hexStr[$i], 16, 2), 4, '0', STR_PAD_LEFT);
    }
    return $binStr;
}

// Function to parse a packet and return the version sum and the index after parsing the packet
function parsePacket($binaryStr, $startIndex = 0) {
    // Extract the version (3 bits) and type ID (3 bits)
    $version = bindec(substr($binaryStr, $startIndex, 3));
    $typeId = bindec(substr($binaryStr, $startIndex + 3, 3));
    $currentIndex = $startIndex + 6;

    // Initialize version sum with current packet's version
    $versionSum = $version;

    // If it's a literal value packet (type ID 4)
    if ($typeId == 4) {
        $literalValue = '';
        while (true) {
            // Each group of 5 bits (first bit is continuation flag, the next 4 are data)
            $group = substr($binaryStr, $currentIndex, 5);
            $literalValue .= substr($group, 1); // Append the last 4 bits
            $currentIndex += 5;
            // If the first bit is 0, it's the last group
            if ($group[0] == '0') {
                break;
            }
        }
        return [$versionSum, $currentIndex];
    }

    // If it's an operator packet
    $lengthTypeId = $binaryStr[$currentIndex];
    $currentIndex++;

    if ($lengthTypeId == '0') {
        // Next 15 bits: the total length of sub-packets in bits
        $subPacketLength = bindec(substr($binaryStr, $currentIndex, 15));
        $currentIndex += 15;
        $endIndex = $currentIndex + $subPacketLength;
        while ($currentIndex < $endIndex) {
            // Recursively parse sub-packets
            list($subVersionSum, $currentIndex) = parsePacket($binaryStr, $currentIndex);
            $versionSum += $subVersionSum;
        }
    } else {
        // Next 11 bits: the number of sub-packets
        $numSubPackets = bindec(substr($binaryStr, $currentIndex, 11));
        $currentIndex += 11;
        for ($i = 0; $i < $numSubPackets; $i++) {
            // Recursively parse sub-packets
            list($subVersionSum, $currentIndex) = parsePacket($binaryStr, $currentIndex);
            $versionSum += $subVersionSum;
        }
    }

    return [$versionSum, $currentIndex];
}

// Main function to decode the hex string and calculate the version sum
function decodeHexPacket($hexStr) {
    // Convert hex to binary
    $binaryStr = hexToBin($hexStr);
    // Parse the binary string and return the total version sum
    list($versionSum, ) = parsePacket($binaryStr);
    return $versionSum;
}

// Read input from file
$hexInput = file_get_contents($inputFile);
$hexInput = trim($hexInput);  // Remove any extra whitespace or newlines

// Decode the packet and output the result
echo "Version sum: " . decodeHexPacket($hexInput) . "\n";


//--- Part Two ---
// Function to convert hex to binary
function hexToBin2($hexStr) {
    $binStr = '';
    for ($i = 0; $i < strlen($hexStr); $i++) {
        $binStr .= str_pad(base_convert($hexStr[$i], 16, 2), 4, '0', STR_PAD_LEFT);
    }
    return $binStr;
}

// Function to parse a packet and return the version sum, value, and the index after parsing the packet
function parsePacket2($binaryStr, $startIndex = 0) {
    // Extract the version (3 bits) and type ID (3 bits)
    $version = bindec(substr($binaryStr, $startIndex, 3));
    $typeId = bindec(substr($binaryStr, $startIndex + 3, 3));
    $currentIndex = $startIndex + 6;

    // Initialize version sum with current packet's version
    $versionSum = $version;

    // Initialize the value
    $value = 0;

    // If it's a literal value packet (type ID 4)
    if ($typeId == 4) {
        $literalValue = '';
        while (true) {
            // Each group of 5 bits (first bit is continuation flag, the next 4 are data)
            $group = substr($binaryStr, $currentIndex, 5);
            $literalValue .= substr($group, 1); // Append the last 4 bits
            $currentIndex += 5;
            // If the first bit is 0, it's the last group
            if ($group[0] == '0') {
                break;
            }
        }
        // Convert the binary literal to decimal
        $value = bindec($literalValue);
        return [$versionSum, $value, $currentIndex];
    }

    // If it's an operator packet
    $lengthTypeId = $binaryStr[$currentIndex];
    $currentIndex++;

    $subPacketValues = [];

    if ($lengthTypeId == '0') {
        // Next 15 bits: the total length of sub-packets in bits
        $subPacketLength = bindec(substr($binaryStr, $currentIndex, 15));
        $currentIndex += 15;
        $endIndex = $currentIndex + $subPacketLength;
        while ($currentIndex < $endIndex) {
            // Recursively parse sub-packets
            list($subVersionSum, $subValue, $currentIndex) = parsePacket2($binaryStr, $currentIndex);
            $versionSum += $subVersionSum;
            $subPacketValues[] = $subValue;
        }
    } else {
        // Next 11 bits: the number of sub-packets
        $numSubPackets = bindec(substr($binaryStr, $currentIndex, 11));
        $currentIndex += 11;
        for ($i = 0; $i < $numSubPackets; $i++) {
            // Recursively parse sub-packets
            list($subVersionSum, $subValue, $currentIndex) = parsePacket2($binaryStr, $currentIndex);
            $versionSum += $subVersionSum;
            $subPacketValues[] = $subValue;
        }
    }

    // Calculate the value based on the type ID
    switch ($typeId) {
        case 0: // Sum
            $value = array_sum($subPacketValues);
            break;
        case 1: // Product
            $value = array_product($subPacketValues);
            break;
        case 2: // Minimum
            $value = min($subPacketValues);
            break;
        case 3: // Maximum
            $value = max($subPacketValues);
            break;
        case 5: // Greater than
            $value = ($subPacketValues[0] > $subPacketValues[1]) ? 1 : 0;
            break;
        case 6: // Less than
            $value = ($subPacketValues[0] < $subPacketValues[1]) ? 1 : 0;
            break;
        case 7: // Equal to
            $value = ($subPacketValues[0] == $subPacketValues[1]) ? 1 : 0;
            break;
    }

    return [$versionSum, $value, $currentIndex];
}

// Main function to decode the hex string and calculate the value of the outermost packet
function decodeHexPacket2($hexStr) {
    // Convert hex to binary
    $binaryStr = hexToBin2($hexStr);
    // Parse the binary string and return the final value
    list($versionSum, $value, ) = parsePacket2($binaryStr);
    return $value;
}

// Read input from file
$hexInput = file_get_contents($inputFile);
$hexInput = trim($hexInput);  // Remove any extra whitespace or newlines

// Decode the packet and output the result (evaluated expression value)
echo "Evaluated value: " . decodeHexPacket2($hexInput) . "\n";
