<?php
// File path
$inputFile = 'input.txt';

//--- Day 22: Reactor Reboot ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));

$lines = explode("\n",$input);
$reactor = [];
$count = 0;
foreach($lines as $line) {
	preg_match("#(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d++),z=(-?\d+)\.\.(-?\d++)#", $line, $code);
	for($x=max(-50,$code[2]);$x<=min(50,$code[3]);$x++) {
		for($y=max(-50,$code[4]);$y<=min(50,$code[5]);$y++) {
			for($z=max(-50,$code[6]);$z<=min(50,$code[7]);$z++) {
				if($code[1] == "on") {
					if(!isset($reactor[$x][$y][$z])) {
						$reactor[$x][$y][$z] = 1;
						$count++;
					}
				}
				else {
					if(isset($reactor[$x][$y][$z])) {
						unset($reactor[$x][$y][$z]);
						$count--;
					}
				}
			}
		}
	}
}
echo "Count: {$count}\n";


//--- Part Two ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));

$lines = explode("\n",$input);
$cubes = [];

$i = 1;
foreach($lines as $line) {
	preg_match("#(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d++),z=(-?\d+)\.\.(-?\d++)#", $line, $code);
	$code[1] = ($code[1] == "on") ? 1 : -1;
	$new = [];
	foreach($cubes as $cube) {
		$ax = max($code[2],$cube[2]);
		$bx = min($code[3],$cube[3]);
		$ay = max($code[4],$cube[4]);
		$by = min($code[5],$cube[5]);
		$az = max($code[6],$cube[6]);
		$bz = min($code[7],$cube[7]);
		if($ax <= $bx && $ay <= $by && $az <= $bz) {
			$overlap = ["", -$cube[1], $ax, $bx, $ay, $by, $az, $bz];
			$new[] = $overlap;
		}
	}
	if($code[1] == 1) $new[] = $code;
	$cubes = array_merge($cubes, $new);
	$i++;
}

$volume = 0;
foreach($cubes as $cube) {
	$volume += $cube[1] * ($cube[3]-$cube[2]+1) * ($cube[5]-$cube[4]+1) * ($cube[7]-$cube[6]+1);
}
echo "Volume: {$volume}";
