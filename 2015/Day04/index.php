<?php

$number = 1;
$number2 = 1;
$input = 'yzbqklnj';

$hash = md5($input . $number);

while(substr($hash, 0, 5) !== "00000") {
    $number++;
    $hash = md5($input . $number);
}

echo 'The number: ' . $number . PHP_EOL;

$hash = md5($input . $number2);

while(substr($hash, 0, 5) !== "000000") {
    $number2++;
    $hash = md5($input . $number2);
}

echo 'The number 2: ' . $number2 . PHP_EOL;