<?php
// File path
$inputFile = 'input.txt';

//--- Day 21: Dirac Dice ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));

preg_match_all("#Player (\d+) starting position: (\d+)#", $input, $matches);
for($i=0;$i<sizeof($matches[1]);$i++) {
	$player[$matches[1][$i]] = ["start" => $matches[2][$i], "score" => 0, "pos" => $matches[2][$i]];
}

$dice = 0;
$turn = 1;
$rolled = 0;
while(1) {
	for($i=1;$i<=3;$i++) {
		$roll[$i] = ++$dice;
		$rolled++;
		if($dice == 100) $dice = 0;
	}
	$rolls = array_sum($roll);
	$space = ($player[$turn]["pos"] + $rolls) % 10;
	if($space == 0) $space = 10;
	$player[$turn]["pos"] = $space;
	$score = $player[$turn]["score"] + $space;
	$player[$turn]["score"] = $score;
	
	if($score>=1000) break;
	
	$turn = ($turn==1) ? 2 : 1;
}
$loser = ($turn==1) ? 2 : 1;
echo "Part 1: " . $player[$loser]["score"]*$rolled . "\n";


//--- Part Two ---
$input = trim(str_replace("\r","",file_get_contents("input.txt")));

preg_match_all("#Player (\d+) starting position: (\d+)#", $input, $matches);
for($i=0;$i<sizeof($matches[1]);$i++) {
	$player[$matches[1][$i]] = ["start" => $matches[2][$i], "score" => 0, "pos" => $matches[2][$i]];
}

for($a=1;$a<=3;$a++) {
	for($b=1;$b<=3;$b++) {
		for($c=1;$c<=3;$c++) {
			if(isset($states[$a+$b+$c]))
				$states[$a+$b+$c]++;
			else
				$states[$a+$b+$c] = 1;
		}
	}
}

function dirac($player, $turn, $universes, $goes) {
	global $states;
	global $wins;
	$inital_score = $player[$turn]["score"];
	$inital_pos = $player[$turn]["pos"];
	foreach($states as $rolls => $times) {
		$space = ($inital_pos + $rolls) % 10;
		if($space == 0) $space = 10;
		$player[$turn]["pos"] = $space;
		$score = $inital_score + $space;
		$player[$turn]["score"] = $score;
		if($score >= 21) {
			$wins[$turn] += ($universes * $times);
		}
		else {
			$next_turn = ($turn==1) ? 2 : 1;
			dirac($player, $next_turn, $universes * $times, $goes+1);
		}
	}
}

$wins = [1=>0,2=>0];
dirac($player, 1, 1, 0);

echo "Most universes: " . max($wins);
