<?php
// File path
$inputFile = 'input.txt';

//--- Day 20: Trench Map ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));

$lines = explode("\n", $input);
$algorithm = $lines[0];
$algorithm = str_replace(array('#','.'),array(1,0),$algorithm);
$in = [];
for($row=2;$row<sizeof($lines);$row++) {
	for($col=0;$col<strlen($lines[2]);$col++) {
		$in[$row-2][$col] = ($lines[$row][$col]=="#") ? 1 : 0;
	}
}

$outer = "0";
for($loop=1;$loop<=2;$loop++) {
	$count = 0;
	$out = [];
	for($row=-1;$row<=sizeof($in);$row++) {
		for($col=-1;$col<=sizeof($in[0]);$col++) {
			$bin = "";
			for($i=-1;$i<=1;$i++) {
				for($j=-1;$j<=1;$j++) {
					$bin .= (isset($in[$row+$i][$col+$j]) ? $in[$row+$i][$col+$j] : $outer);
				}
			}
			$value = $algorithm[base_convert($bin,2,10)];
			$count += $value;
			$out[$row+1][$col+1] = $value;
		}
	}
	$bin = str_pad("",9,$outer);
	$outer = $algorithm[base_convert($bin,2,10)];
	$in = $out;
}

echo "Answer " . $count . "\n";

//--- Part Two ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));

$lines = explode("\n", $input);
$algorithm = $lines[0];
$algorithm = str_replace(array('#','.'),array(1,0),$algorithm);
$in = [];
for($row=2;$row<sizeof($lines);$row++) {
	for($col=0;$col<strlen($lines[2]);$col++) {
		$in[$row-2][$col] = ($lines[$row][$col]=="#") ? 1 : 0;
	}
}

$outer = "0";
for($loop=1;$loop<=50;$loop++) {
	$count = 0;
	$out = [];
	for($row=-1;$row<=sizeof($in);$row++) {
		for($col=-1;$col<=sizeof($in[0]);$col++) {
			$bin = "";
			for($i=-1;$i<=1;$i++) {
				for($j=-1;$j<=1;$j++) {
					$bin .= (isset($in[$row+$i][$col+$j]) ? $in[$row+$i][$col+$j] : $outer);
				}
			}
			$value = $algorithm[base_convert($bin,2,10)];
			$count += $value;
			$out[$row+1][$col+1] = $value;
		}
	}
	$bin = str_pad("",9,$outer);
	$outer = $algorithm[base_convert($bin,2,10)];
	$in = $out;
}

echo "Answer " . $count;
