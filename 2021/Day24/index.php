<?php
// File path
$inputFile = 'input.txt';

//--- Day 24: Arithmetic Logic Unit ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));

$lines = explode("\n",$input);
$var = ['w'=>0,'x'=>0,'y'=>0,'z'=>0];
$inp = array_fill(1,14,9);
$pointer = 1;

$debug = isset($_GET['debug']);

$x = 0;
$y = 0;
$dump = [];
$lets = [];
for($i=0;$i<14;$i++) {
	$l = chr(65+$i);
	$stuff = [];
	$stuff[] = explode(" ",$lines[($i*18)+4])[2];
	$stuff[] = explode(" ",$lines[($i*18)+5])[2];
	$stuff[] = explode(" ",$lines[($i*18)+15])[2];
	if($stuff[0] == 1) {
		$dump[] = [$l,$stuff[2]];
	}
	else {
		$d = array_pop($dump);
		$lets[] = [$l,$d[0],$d[1]+$stuff[1]];
	}
}

$min = $max = array_fill(1,14,0);
foreach($lets as $l) {
	$a = ord($l[0])-64;
	$b = ord($l[1])-64;
	if($l[2]>0) {
		$max[$a] = 9;
		$max[$b] = 9 - $l[2];
		$min[$b] = 1;
		$min[$a] = 1 + $l[2];
	}
	else {
		$max[$b] = 9;
		$max[$a] = 9 + $l[2];
		$min[$a] = 1;
		$min[$b] = 1 - $l[2];
	}
}
echo "Max: " . implode("", $max) .  "\n";

//--- Part Two ---
echo "Min: " . implode("", $min) .  "\n";