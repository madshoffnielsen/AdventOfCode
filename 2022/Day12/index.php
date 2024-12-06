<?php

$file = file("input.txt");
foreach ($file as $line) {
    $_input[] = trim($line);
}

// filled out while building the graph...
$s_key = '';
$e_key = '';
$a_key = [];
$graph = build_graph($_input);

$a_steps = [];
foreach (array_keys($a_key) as $a)
    if ($path = BFS($graph, $a, $e_key))
        $a_steps[$a] = count($path) - 1;
asort($a_steps);

echo "part 1: {$a_steps[$s_key]}\n";
echo "part 2: {$a_steps[array_key_first($a_steps)]}\n";

function _v($x, $y) // get value from input, look for special chars...
{
    global $_input, $s_key, $e_key, $a_key;
    $v = $_input[$y][$x];
    if ($v == 'S')
    {
        if (!$s_key)
        {
            $s_key = json_encode([$x,$y]);
            $a_key[$s_key] = 1;
        }
        return 'a';
    }
    elseif ($v == "E")
    {
        if (!$e_key) $e_key = json_encode([$x,$y]);
        return 'z';
    }
    elseif ($v == 'a') $a_key[json_encode([$x,$y])] = 1;

    return $v;
}

function adj($v, $v2): bool
{
    // v2 is one higher or less than v...
    return ord($v2) - ord($v) <= 1;
}

function build_graph(&$_input)
{
    $graph = []; // adjacency list...
    for ($x = 0, $w = strlen($_input[0]); $x < $w; $x++)
        for ($y = 0, $h = count($_input); $y < $h; $y++)
        {
            // key...
            $k = json_encode([$x, $y]);
            if (!isset($graph[$k])) $graph[$k] = [];
            // value...
            $v = _v($x, $y);
            // left...
            if ($x > 0 && adj($v, _v($x - 1, $y)))
                $graph[$k][] = json_encode([$x - 1, $y]);
            // right...
            if ($x < $w - 1 && adj($v, _v($x + 1, $y)))
                $graph[$k][] = json_encode([$x + 1, $y]);
            // up...
            if ($y > 0 && adj($v, _v($x, $y - 1)))
                $graph[$k][] = json_encode([$x, $y - 1]);
            // down...
            if ($y < $h - 1 && adj($v, _v($x, $y + 1)))
                $graph[$k][] = json_encode([$x, $y + 1]);
        }
    return $graph;
}

function BFS($graph, $start, $end = null, array &$visited = null): array
{
    $visited = array();
    $q = new SplQueue();
    $q->enqueue(array($start));
    $visited[$start] = 0;
    while ($q->count())
    {
        $path = $q->dequeue();
        $node = $path[count($path)-1];
        if ($node === $end) return $path;
        foreach ($graph[$node] as $adj)
        {
            if (!isset($visited[$adj]))
            {
                $visited[$adj] = count($path);
                $_p = $path;
                $_p[] = $adj;
                $q->enqueue($_p);
            }
        }
    }
    return [];
}
