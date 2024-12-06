<?php
// File path
$inputFile = 'input.txt';

//--- Day 18: Snailfish ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));

function add($a,$b) {
	return "[{$a},{$b}]";
}

function reduce($a) {
	$o = $a;
	$a = parse($a);
	if($a!=$o) {
		$a = reduce($a);
	}
	else {
		$a = split($a);
		if($a!=$o) {
			$a = reduce($a);
		}
	}
	return $a;		
}

function parse($a) {
	preg_match_all("#\[|\]|,|\d+#", $a, $matches);
	$stack = $matches[0];
	$opened = 0;
	for($i=0;$i<sizeof($stack)-2;$i++) {
		$v = $stack[$i];
		if($v=='[') $opened++;
		else if($v==']') $opened--;
		else if(is_numeric($v) && $stack[$i+1] == ',' && is_numeric($stack[$i+2]) && $opened > 4) {
			//work backwards to find left int
			for($j=$i-1;$j>=0;$j--) {
				if(is_numeric($stack[$j])) {
					$stack[$j]+= $v;
					break;
				}
			}
			//work forward to find right int
			for($j=$i+3;$j<sizeof($stack);$j++) {
				if(is_numeric($stack[$j])) {
					$stack[$j]+= $stack[$i+2];
					break;
				}
			}
			//cut middle out
			array_splice($stack, $i-1,5,0);
			break;
		}
	}
	return implode("", $stack);
}

function split($a) {
	preg_match_all("#\[|\]|,|\d+#", $a, $matches);
	$stack = $matches[0];
	for($i=0;$i<sizeof($stack);$i++) {
		$v = $stack[$i];
		if(is_numeric($v) && (int)$v >= 10) {
			array_splice($stack, $i, 1, ['[',floor($v/2),',',ceil($v/2),']']);
			break;
		}
	}
	return implode("", $stack);
}

function magnitude($a) {
	$a = preg_replace_callback(
		"#\[(\d+),(\d+)\]#",
		function($matches) {
			return ($matches[1]*3) + ($matches[2]*2);
		},
		$a
	);
	if(strpos($a,',') !== false) {
		$a = magnitude($a);
	}
	return $a;
}

$lines = explode("\n", $input);
$sum = $lines[0];
for($i=1;$i<sizeof($lines);$i++) {
	$sum = reduce(add($sum, $lines[$i]));
}
echo "Magnitude: " . magnitude($sum) . "\n";


//--- Part Two ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));

$lines = explode("\n", $input);
$max = 0;

for($i=0;$i<sizeof($lines);$i++) {
	for($j=0;$j<sizeof($lines);$j++) {
		if($i!=$j) {
			$sum = magnitude(reduce(add($lines[$i],$lines[$j])));
			$max = max($max,$sum);
		}
	}
}
echo "Max Magnitude: " . $max . "\n";
