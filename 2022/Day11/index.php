<?php
include 'BigInteger.php';

use PHP\Math\BigInteger\BigInteger;

$totalScore = 0;

$inspections = array_fill(0, 8, 0);
$inspectionsPart2 = array_fill(0, 8, 0);

$items = array_fill(0, 8, []);
$itemsPart2 = array_fill(0, 8, []);
$operation = array_fill(0, 8, '');
$operationValue = array_fill(0, 8, 0);
$test = array_fill(0, 8, 0);
$true = array_fill(0, 8, 0);
$false = array_fill(0, 8, 0);

$globalModulus = 1;

$currentMonkey;

$file = file("input.txt");
if ($file) {
    foreach ($file as $line) {
        $args = explode(' ', trim($line));

        if (count($args) == 1) {
            continue;
        }

        if ($args[0] == 'Monkey') {
            $currentMonkey = str_replace(':', '', $args[1]);
        }
        if ($args[0] == 'Starting') {
            $values = substr($line, 18);
            $its = explode(', ', $values);
            foreach ($its as $key => $value) {
                $items[$currentMonkey][] = new BigInteger($value);
                $itemsPart2[$currentMonkey][] = new BigInteger($value);
            }
        }
        if ($args[0] == 'Operation:') {
            $operation[$currentMonkey] = $args[4];
            $operationValue[$currentMonkey] = $args[5];
        }
        if ($args[0] == 'Test:') {
            $test[$currentMonkey] = $args[3];
            $globalModulus *= $test[$currentMonkey];
        }
        if ($args[1] == 'true:') {
            $true[$currentMonkey] = $args[5];
        }
        if ($args[1] == 'false:') {
            $false[$currentMonkey] = $args[5];
        }
    }

    for ($round=0; $round < 20; $round++) {
        foreach ($inspections as $key => $value) {
            while(count($items[$key]) > 0) {
                $item = array_shift($items[$key]);
                $inspections[$key]++;

                $worryLevel = new BigInteger($item->getValue());

                if ($operationValue[$key] == 'old') {
                    if ($operation[$key] == '*') {
                        $worryLevel->multiply($item->getValue());
                    }
                    else {
                        $worryLevel->add($item->getValue());
                    }
                }
                else {
                    if ($operation[$key] == '*') {
                        $worryLevel->multiply($operationValue[$key]);
                    }
                    else {
                        $worryLevel->add($operationValue[$key]);
                    }
                }
                $worryLevel->divide(3);

                $mod = new BigInteger($worryLevel->getValue());

                if ($mod->mod($test[$key])->getValue() == 0) {
                    array_push($items[$true[$key]], $worryLevel);
                }
                else {
                    array_push($items[$false[$key]], $worryLevel);
                }
            }
        }
    }

    echo 'Result part 1:' . PHP_EOL . '--------------------' . PHP_EOL;
    foreach ($inspections as $key => $value) {
        echo 'Monkey ' . $key . ' inspected items ' . $value . ' times.' . PHP_EOL;
    }
    echo '--------------------' . PHP_EOL;

    $temp = new BigInteger(0);

    for ($round=0; $round < 10000; $round++) {
        foreach ($inspectionsPart2 as $key => $value) {
            while(count($itemsPart2[$key]) > 0) {
                $item = array_shift($itemsPart2[$key]);
                $inspectionsPart2[$key]++;

                $temp->setValue($item->getValue());
                $temp->divide($globalModulus);
                $temp->multiply($globalModulus);
                $item->subtract($temp->getValue());

                if ($operationValue[$key] == 'old') {
                    if ($operation[$key] == '*') {
                        $item->multiply($item->getValue());
                    }
                    else {
                        $item->add($item->getValue());
                    }
                }
                else {
                    if ($operation[$key] == '*') {
                        $item->multiply($operationValue[$key]);
                    }
                    else {
                        $item->add($operationValue[$key]);
                    }
                }

                $mod = intval($test[$key]);
                $temp->setValue($item->getValue());
                $temp->divide($mod);
                $temp->multiply($mod);

                if ($item->getValue() == $temp->getValue()) {
                    array_push($itemsPart2[$true[$key]], $item);
                }
                else {
                    array_push($itemsPart2[$false[$key]], $item);
                }
            }
        }
        if ($round%1000 == 0) {
            echo 'Part 2 round: ' . $round / 100 . '%' . PHP_EOL;
        }
    }

    echo 'Result part 2:' . PHP_EOL . '--------------------' . PHP_EOL;
    foreach ($inspectionsPart2 as $key => $value) {
        echo 'Monkey ' . $key . ' inspected items ' . $value . ' times.' . PHP_EOL;
    }
}
