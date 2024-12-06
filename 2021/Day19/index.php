<?php
// File path
$inputFile = 'input.txt';

//--- Day 19: Beacon Scanner ---
function rotations($beacon) {
	[$x,$y,$z] = $beacon;
	return [
		[ $x, $y, $z],
		[ $x, $z,-$y],
		[ $x,-$y,-$z],
		[ $x,-$z, $y],
		
		[-$x,-$y, $z],
		[-$x,-$z,-$y],
		[-$x, $y,-$z],
		[-$x, $z, $y],
		
		[ $y,-$x, $z],
		[ $y, $z, $x],
		[ $y, $x,-$z],
		[ $y,-$z,-$x],
		
		[-$y, $x, $z],
		[-$y,-$z, $x],
		[-$y,-$x,-$z],
		[-$y, $z,-$x],
		
		[ $z, $y,-$x],
		[ $z, $x, $y],
		[ $z,-$y, $x],
		[ $z,-$x,-$y],
		
		[-$z,-$y,-$x],
		[-$z,-$x, $y],
		[-$z, $y, $x],
		[-$z, $x,-$y],
	];
}

$input = trim(str_replace("\r","",file_get_contents("input.txt")));

$lines = explode("\n", $input);
$id = -1;
foreach($lines as $line) {
	if(preg_match("#--- scanner (\d+) ---#", $line, $matches)) {
		$id = $matches[1];
		$tofind[] = $matches[1];
	}
	else if(trim($line) !== "") {
		$scanner[$id][] = explode(",",$line);
		$strings[$id][] = $line;
	}
}

$diffs = [];
$diffs_lib = [];
for($i=0;$i<sizeof($scanner);$i++) {
	$scan_diff = [];
	for($x=0;$x<sizeof($scanner[$i]);$x++) {
		for($y=$x+1;$y<sizeof($scanner[$i]);$y++) {
			$a = $scanner[$i][$x];
			$b = $scanner[$i][$y];
			$distance = ($b[0]-$a[0])**2 + ($b[1]-$a[1])**2 + ($b[2]-$a[2])**2;
			$scan_diff[] = $distance;
			$diffs_lib[$i][$distance] = [$a,$b];
		}
	}
	sort($scan_diff);
	$diffs[] = $scan_diff;
}

$loc[0] = [0,0,0];
$toscan[] = 0;
$found[] = 0;

while(sizeof($toscan)) {
	$i = array_pop($toscan);
	for($j=0;$j<sizeof($diffs);$j++) {
		if(!in_array($j,$found)) {
			$union = array_intersect($diffs[$i], $diffs[$j]);
			if(sizeof($union) >= 66) { 
				$temp = [];
				$offsets = [];
				foreach($union as $u) {
					$key_ia = implode(",",$diffs_lib[$i][$u][0]);
					$key_ib = implode(",",$diffs_lib[$i][$u][1]);
					$key_ja = implode(",",$diffs_lib[$j][$u][0]);
					$key_jb = implode(",",$diffs_lib[$j][$u][1]);
					if(isset($temp["{$key_ia}|{$key_ja}"]))
                        $temp["{$key_ia}|{$key_ja}"]++;
                    else
                        $temp["{$key_ia}|{$key_ja}"] = 1;
                    if(isset($temp["{$key_ib}|{$key_ja}"]))
                        $temp["{$key_ib}|{$key_ja}"]++;
                    else
                        $temp["{$key_ib}|{$key_ja}"] = 1;
                    if(isset($temp["{$key_ia}|{$key_jb}"]))
                        $temp["{$key_ia}|{$key_jb}"]++;
                    else
                        $temp["{$key_ia}|{$key_jb}"] = 1;
                    if(isset($temp["{$key_ib}|{$key_jb}"]))
                        $temp["{$key_ib}|{$key_jb}"]++;
                    else
                        $temp["{$key_ib}|{$key_jb}"] = 1;
				}
				
				foreach($temp as $t => $v) {
					if($v>=11) { 
						[$key_i,$key_j] = explode("|",$t);
						[$ix,$iy,$iz] = explode(",",$key_i);
						$beacon_j = explode(",",$key_j);
						$rotations = rotations($beacon_j);
						for($r=0;$r<24;$r++) {
							[$jx,$jy,$jz] = $rotations[$r];
							$dx = $ix-$jx;
							$dy = $iy-$jy;
							$dz = $iz-$jz;
                            if (isset($offsets[$r]["{$dx},{$dy},{$dz}"])){
							    $offsets[$r]["{$dx},{$dy},{$dz}"]++;
                            }
                            else {
                                $offsets[$r]["{$dx},{$dy},{$dz}"] = 1;
                            }

						}
					}
				}
				$rot = -1;
				foreach($offsets as $r => $v) {
					if(sizeof($v) == 1) {
						$rot = $r;
						$off = explode(",",key($v));
					}
				}
				if($rot != -1) {
					$loc[$j] = $off;
					for($t=0;$t<sizeof($scanner[$j]);$t++) {
						$scan = $scanner[$j][$t];
						$rots = rotations($scan);
						$new  = [$rots[$rot][0]+$loc[$j][0],$rots[$rot][1]+$loc[$j][1],$rots[$rot][2]+$loc[$j][2]];
						$scanner[$j][$t] = $new;
						$strings[$j][$t] = implode(",",$new);
					}
					for($x=0;$x<sizeof($scanner[$j]);$x++) {
						for($y=$x+1;$y<sizeof($scanner[$j]);$y++) {
							$a = $scanner[$j][$x];
							$b = $scanner[$j][$y];
							$distance = ($b[0]-$a[0])**2 + ($b[1]-$a[1])**2 + ($b[2]-$a[2])**2;
							$diffs_lib[$j][$distance] = [$a,$b];
						}
					}
					$found[] = $j;
					$toscan[] = $j;
					$uni = array_intersect($strings[$i],$strings[$j]);
				}
			}
		}
	}
}

$unique = [];
foreach($strings as $id => $scan) {
	foreach($scan as $beacon) {
		if(!in_array($beacon,$unique)) $unique[] = $beacon;
	}
}
echo "Beacons: " . sizeof($unique) . "\n";

//--- Part Two ---
$max = 0;
for($i=0;$i<sizeof($loc);$i++) {
	for($b=$i+1;$b<sizeof($loc);$b++) {
		$manhattan = abs($loc[$i][0]-$loc[$b][0]) + abs($loc[$i][1]-$loc[$b][1]) + abs($loc[$i][2]-$loc[$b][2]);
		$max = max($max,$manhattan);
	}
}
echo "Max Manhattan: {$max}\n";
