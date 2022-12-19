<?php

$number = 1;
$number2 = 1;
$input = 'yzbqklnj';

$hash = md5($input . $number);

while(substr($hash, 0, 5) !== "00000") {
    $number++;
    $hash = md5($input . $number);
}

echo 'Number 1: ' . $number . PHP_EOL;

$hash = md5($input . $number2);

while(substr($hash, 0, 6) !== "000000") {
    $number2++;
    $hash = md5($input . $number2);
}

echo 'Number 2: ' . $number2 . PHP_EOL;
