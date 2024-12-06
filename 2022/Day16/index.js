function maxPressureReleased (input, startTime) {
    const score = search(input, startTime)
    return score[0][1]
  }

  function maxPressureReleased2 (input, startTime) {
    const score = search(input, startTime)
    let max = 0
    for (let j = 1; j < score.length; j++) {
      for (let i = 0; i < j; i++) {
        if (score[i][1] * 2 < max) break
        const hashA = score[i][0]
        const hashB = score[j][0]
        if (hashA & hashB) continue
        const total = score[i][1] + score[j][1]
        if (total > max) max = total
      }
    }
    return max
  }

  function search (input, startTime) {
    const valves = getValves(input)
    const openable = input.filter(row => row.rate > 0)
    const shortestPath = getShortestPath(valves, openable)

    const score = []
    const unvisited = []
    unvisited.push([0, 'AA', startTime, 0])

    while (unvisited.length > 0) {
      const [visited, next, time, released, extras] = unvisited.pop()
      openable.forEach(row => {
        if (visited & row.hash) return
        score.push([visited, released])
        const distance = shortestPath[next][row.from]
        const nextTime = time - distance - 1
        if (nextTime > 0) {
          unvisited.push([
            visited + row.hash,
            row.from,
            nextTime,
            released + nextTime * row.rate,
            extras
          ])
        }
      })
    }

    return score.sort((a, b) => b[1] - a[1])
  }

  function getShortestPath (valves, openable) {
    function findShortestPath (start) {
      const visited = {}
      const unvisited = []
      unvisited.push([valves[start], 0])
      while (unvisited.length > 0) {
        const [next, steps] = unvisited.shift()
        if (next.from in visited) {
          if (steps >= visited[next.from]) continue
          else visited[next.from] = steps
        } else {
          visited[next.from] = steps
        }
        Object.keys(next.to).forEach(id =>
          unvisited.push([valves[id], steps + next.to[id]])
        )
      }
      delete visited[start]
      return visited
    }

    const shortest = {}
    shortest.AA = findShortestPath('AA')
    openable.forEach(row => {
      shortest[row.from] = findShortestPath(row.from)
    })
    return shortest
  }

  function getValves (input) {
    const valves = {}
    let hash = 1
    input.forEach(row => {
      valves[row.from] = row
      if (row.rate > 0) {
        row.hash = hash
        hash *= 2
      }
    })

    function preprocessInputRowTo (row, path = []) {
      if (!Array.isArray(row.to)) return row.to
      const to = {}
      row.to.forEach(id => {
        if (path.includes(id)) return
        const next = valves[id]
        const steps =
          next.rate > 0
            ? { [id]: 0 }
            : preprocessInputRowTo(next, [...path, row.from])
        Object.keys(steps).forEach(id => {
          if (id in to) to[id] = Math.min(to[id], steps[id] + 1)
          else to[id] = steps[id] + 1
        })
      })
      delete to[row.from]
      return to
    }

    input.forEach(row => {
      row.to = preprocessInputRowTo(row)
    })

    return valves
  }

  function parse (line) {
    const matched = line.match(
      /^Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)$/
    )
    return {
      from: matched[1],
      to: matched[3].split(', '),
      rate: +matched[2]
    }
  }

  const test = `
  Valve OA has flow rate=0; tunnels lead to valves VP, VM
Valve GA has flow rate=13; tunnel leads to valve KV
Valve WD has flow rate=0; tunnels lead to valves SH, XQ
Valve TE has flow rate=0; tunnels lead to valves OY, DO
Valve JR has flow rate=0; tunnels lead to valves TR, LY
Valve JQ has flow rate=0; tunnels lead to valves TD, DZ
Valve VH has flow rate=6; tunnels lead to valves WY, YQ, NU
Valve NX has flow rate=0; tunnels lead to valves XQ, MN
Valve XL has flow rate=0; tunnels lead to valves AA, FA
Valve QY has flow rate=0; tunnels lead to valves NU, DO
Valve KV has flow rate=0; tunnels lead to valves GA, XQ
Valve NK has flow rate=0; tunnels lead to valves XW, XQ
Valve JU has flow rate=0; tunnels lead to valves QH, TB
Valve XZ has flow rate=0; tunnels lead to valves AA, SH
Valve XQ has flow rate=18; tunnels lead to valves GK, NX, WD, KV, NK
Valve VM has flow rate=19; tunnels lead to valves LY, OA, OY, AE
Valve LE has flow rate=0; tunnels lead to valves MN, NS
Valve HO has flow rate=0; tunnels lead to valves GO, QH
Valve PX has flow rate=0; tunnels lead to valves MN, VP
Valve MN has flow rate=4; tunnels lead to valves LE, UX, TB, NX, PX
Valve VB has flow rate=0; tunnels lead to valves XM, AA
Valve VP has flow rate=21; tunnels lead to valves XM, WT, BG, PX, OA
Valve KI has flow rate=15; tunnels lead to valves XU, MT
Valve NU has flow rate=0; tunnels lead to valves QY, VH
Valve WT has flow rate=0; tunnels lead to valves SH, VP
Valve OY has flow rate=0; tunnels lead to valves VM, TE
Valve VS has flow rate=0; tunnels lead to valves QH, SH
Valve XM has flow rate=0; tunnels lead to valves VB, VP
Valve HI has flow rate=17; tunnel leads to valve TD
Valve TB has flow rate=0; tunnels lead to valves JU, MN
Valve BG has flow rate=0; tunnels lead to valves VP, GK
Valve HN has flow rate=16; tunnel leads to valve BO
Valve MT has flow rate=0; tunnels lead to valves KI, BO
Valve OX has flow rate=0; tunnels lead to valves DZ, ZF
Valve QH has flow rate=5; tunnels lead to valves FA, DW, VS, JU, HO
Valve YQ has flow rate=0; tunnels lead to valves VH, AE
Valve DW has flow rate=0; tunnels lead to valves ML, QH
Valve WY has flow rate=0; tunnels lead to valves HS, VH
Valve GO has flow rate=0; tunnels lead to valves HO, DO
Valve UX has flow rate=0; tunnels lead to valves AA, MN
Valve AE has flow rate=0; tunnels lead to valves YQ, VM
Valve DZ has flow rate=9; tunnels lead to valves HS, OX, JQ
Valve NS has flow rate=0; tunnels lead to valves SH, LE
Valve LY has flow rate=0; tunnels lead to valves JR, VM
Valve BO has flow rate=0; tunnels lead to valves HN, MT
Valve HS has flow rate=0; tunnels lead to valves WY, DZ
Valve XW has flow rate=0; tunnels lead to valves NK, AA
Valve DO has flow rate=11; tunnels lead to valves TE, XU, ZF, QY, GO
Valve FA has flow rate=0; tunnels lead to valves XL, QH
Valve AA has flow rate=0; tunnels lead to valves VB, XL, XZ, XW, UX
Valve VW has flow rate=14; tunnel leads to valve ML
Valve SH has flow rate=8; tunnels lead to valves NS, WT, XZ, VS, WD
Valve XU has flow rate=0; tunnels lead to valves DO, KI
Valve ZF has flow rate=0; tunnels lead to valves OX, DO
Valve GK has flow rate=0; tunnels lead to valves XQ, BG
Valve ML has flow rate=0; tunnels lead to valves VW, DW
Valve TD has flow rate=0; tunnels lead to valves HI, JQ
Valve TR has flow rate=25; tunnel leads to valve JR
  `.trim().split('\n').map(parse)

  console.log(maxPressureReleased(test, 30))
  console.log(maxPressureReleased2(test, 26))