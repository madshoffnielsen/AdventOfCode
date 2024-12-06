<?php

$_fp = fopen("input.txt", "r");

$R = [];
$y_max = PHP_INT_MIN;

while (!feof($_fp) && $s = trim(fgets($_fp)))
{
    $s = explode(' -> ', $s);
    $_r = [];
    foreach($s as $k => $v)
    {
        list($x, $y) = explode(',', $v);
        if ($y > $y_max) $y_max = $y;
        $_r[] = [(int)$x, (int)$y];
    }
    $R[] = $_r;
}

$w = 500;
$dx = -(500-floor($w/2));
$h = $y_max + 2;

$C = array_fill(0, $h, array_fill(0, $w, '.'));
$C[0][500+$dx] = '+';
$C[] = array_fill(0, $w, '#');

foreach ($R as $v)
{
    list($x1, $y1) = array_shift($v);
    while(count($v))
    {
        list($x2, $y2) = array_shift($v);
        if ($x1 < $x2)
            array_splice($C[$y1], $x1+$dx, $x2-$x1+1, array_fill(0, $x2-$x1+1, '#'));
        elseif ($x2 < $x1)
            array_splice($C[$y2], $x2+$dx, $x1-$x2+1, array_fill(0, $x1-$x2+1, '#'));
        elseif ($y1 != $y2)
            foreach(range($y1, $y2) as $_y) $C[$_y][$x1+$dx] = '#';
        list($x1, $y1) = [$x2, $y2];
    }
}

$part1 = $part2 = $sand = 0;

while (true)
{
    list($px, $py) = [500+$dx, 0];
    while (true)
    {
        if ($py > $y_max && !$part1) { $part1 = $sand; }
        // move sand...
        if ($C[$py+1][$px] == '.') $py++;
        elseif ($C[$py+1][$px-1] == '.') { $py++; $px--; }
        elseif ($C[$py+1][$px+1] == '.') { $py++; $px++; }
        else { $C[$py][$px] = 'o'; $sand++; break; }
    }
    if (!$py) { $part2 = $sand; break; }
}

echo "part 1: {$part1}\n";
echo "part 2: {$part2}\n";
