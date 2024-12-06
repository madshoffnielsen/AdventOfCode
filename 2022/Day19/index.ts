const start = performance.now();

const sampleInput = `Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.`;
const input = `Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 7 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 4 ore and 18 obsidian.
Blueprint 3: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 4: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 5: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 6: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 3 ore and 7 obsidian.
Blueprint 7: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 19 clay. Each geode robot costs 2 ore and 20 obsidian.
Blueprint 8: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 13 clay. Each geode robot costs 2 ore and 20 obsidian.
Blueprint 9: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 8 clay. Each geode robot costs 2 ore and 14 obsidian.
Blueprint 10: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 11: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 5 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 12: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 2 ore and 18 obsidian.
Blueprint 13: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 14: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 15: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 16: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 17 obsidian.
Blueprint 17: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 18: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 9 clay. Each geode robot costs 3 ore and 9 obsidian.
Blueprint 19: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 10 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 20: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 13 clay. Each geode robot costs 3 ore and 12 obsidian.
Blueprint 21: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 15 clay. Each geode robot costs 4 ore and 9 obsidian.
Blueprint 22: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 23: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 4 ore and 12 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 15 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 25: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 11 clay. Each geode robot costs 2 ore and 16 obsidian.
Blueprint 26: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 3 ore and 7 obsidian.
Blueprint 27: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 28: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 10 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 29: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 17 clay. Each geode robot costs 2 ore and 13 obsidian.
Blueprint 30: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 4 ore and 8 obsidian.`;

// ===========================================================
// PART 1
// ===========================================================

let answer1 = 0;
const rows = sampleInput.split(`\n`);

type Blueprint = {
  blueprintId: number;
  oreRobotCostOre: number;
  clayRobotCostOre: number;
  obsidianRobotCostOre: number;
  obsidianRobotCostClay: number;
  geodeRobotCostOre: number;
  geodeRobotCostObsidian: number;
};

const parsed = [] as Array<Blueprint>;

for (const row of rows) {
  const [
    ,
    blueprintId,
    oreRobotCostOre,
    clayRobotCostOre,
    obsidianRobotCostOre,
    obsidianRobotCostClay,
    geodeRobotCostOre,
    geodeRobotCostObsidian,
  ] =
    /Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian./
      .exec(row)
      ?.map(Number) ?? [];
  parsed.push({
    blueprintId,
    oreRobotCostOre,
    clayRobotCostOre,
    obsidianRobotCostOre,
    obsidianRobotCostClay,
    geodeRobotCostOre,
    geodeRobotCostObsidian,
  });
}

type State = {
  minutesLeft: number;
  oreRobots: number;
  ore: number;
  clayRobots: number;
  clay: number;
  obsidianRobots: number;
  obsidian: number;
  geodeRobots: number;
  geodes: number;
};

function evaluateBlueprint(blueprint: Blueprint, totalMinutes: number): number {
  const visited = new Array<number[]>();
  let i = 0;
  const queue = new Array<State>();
  queue.push({
    minutesLeft: totalMinutes,
    oreRobots: 1,
    ore: 0,
    clayRobots: 0,
    clay: 0,
    obsidianRobots: 0,
    obsidian: 0,
    geodeRobots: 0,
    geodes: 0,
  });
  const v1b = 7;
  const v2b = 12;
  let best = 0;
  const rgMax = [] as Array<number>;
  for (let i = 0; i < 1e9 && queue.length > 0; i++) {
    const {
      minutesLeft,
      oreRobots,
      ore,
      clayRobots,
      clay,
      obsidianRobots,
      obsidian,
      geodeRobots,
      geodes,
    } = queue.pop()!;

    // Cases
    if (minutesLeft === 0) {
      best = Math.max(geodes, best);
      continue;
    }

    // Saw this suggestion: If can't beat best w/ max effort, quit out.
    let rg = rgMax[minutesLeft];
    if (rg === undefined) {
      rg = 0;
      for (let m = 1; m <= minutesLeft; m++) {
        rg += m * (minutesLeft - m);
      }
      rgMax[minutesLeft] = rg;
    }
    const theoreticalBest = geodes + geodeRobots * minutesLeft + rg;
    if (theoreticalBest <= best) {
      continue;
    }

    // Check visisted.
    const visitedKey1 =
      ((minutesLeft & ((1 << (v1b + 1)) - 1)) << (v1b * 0)) +
      ((oreRobots & ((1 << (v1b + 1)) - 1)) << (v1b * 1)) +
      ((clayRobots & ((1 << (v1b + 1)) - 1)) << (v1b * 2)) +
      ((obsidianRobots & ((1 << (v1b + 1)) - 1)) << (v1b * 3)) +
      ((geodeRobots & ((1 << (v1b + 1)) - 1)) << (v1b * 4));
    const visitedKey2 =
      ((ore & ((1 << (v2b + 1)) - 1)) << (v2b * 0)) +
      ((clay & ((1 << (v2b + 1)) - 1)) << (v2b * 1)) +
      ((obsidian & ((1 << (v2b + 1)) - 1)) << (v2b * 2)) +
      ((geodes & ((1 << (v2b + 1)) - 1)) << (v2b * 3));
    const isVisited = visited[visitedKey1]?.[visitedKey2];
    if (isVisited > 0) {
      continue;
    }
    if (!visited[visitedKey1]) {
      visited[visitedKey1] = new Array<number>();
    }
    visited[visitedKey1][visitedKey2] = 1;

    // Option 1 - Buy geode robot if possible.
    if (
      blueprint.geodeRobotCostOre <= ore &&
      blueprint.geodeRobotCostObsidian <= obsidian
    ) {
      queue.push({
        minutesLeft: minutesLeft - 1,
        oreRobots,
        ore: ore + oreRobots - blueprint.geodeRobotCostOre,
        clayRobots,
        clay: clay + clayRobots,
        obsidianRobots,
        obsidian: obsidian + obsidianRobots - blueprint.geodeRobotCostObsidian,
        geodeRobots: geodeRobots + 1,
        geodes: geodes + geodeRobots,
      });
      // Stop here, because no need to hoard obsidian.
      continue;
    }
    let boughtRobot = false;

    // Option 2 - Buy obsidian robot
    if (
      blueprint.obsidianRobotCostClay <= clay &&
      blueprint.obsidianRobotCostOre <= ore
    ) {
      queue.push({
        minutesLeft: minutesLeft - 1,
        oreRobots,
        ore: ore + oreRobots - blueprint.obsidianRobotCostOre,
        clayRobots,
        clay: clay + clayRobots - blueprint.obsidianRobotCostClay,
        obsidianRobots: obsidianRobots + 1,
        obsidian: obsidian + obsidianRobots,
        geodeRobots,
        geodes: geodes + geodeRobots,
      });
      boughtRobot = true;
    }

    // Option 3 - buy clay robot.
    if (blueprint.clayRobotCostOre <= ore) {
      queue.push({
        minutesLeft: minutesLeft - 1,
        oreRobots,
        ore: ore + oreRobots - blueprint.clayRobotCostOre,
        clayRobots: clayRobots + 1,
        clay: clay + clayRobots,
        obsidianRobots,
        obsidian: obsidian + obsidianRobots,
        geodeRobots,
        geodes: geodes + geodeRobots,
      });
      boughtRobot = true;
    }

    // Option 4 - buy ore robot.
    if (blueprint.oreRobotCostOre <= ore) {
      queue.push({
        minutesLeft: minutesLeft - 1,
        oreRobots: oreRobots + 1,
        ore: ore + oreRobots - blueprint.oreRobotCostOre,
        clayRobots,
        clay: clay + clayRobots,
        obsidianRobots,
        obsidian: obsidian + obsidianRobots,
        geodeRobots,
        geodes: geodes + geodeRobots,
      });
      boughtRobot = true;
    }

    // Option 5 - Do nothing. Let robots collect things.
    if (!boughtRobot) {
      queue.push({
        minutesLeft: minutesLeft - 1,
        oreRobots,
        ore: ore + oreRobots,
        clayRobots,
        clay: clay + clayRobots,
        obsidianRobots,
        obsidian: obsidian + obsidianRobots,
        geodeRobots,
        geodes: geodes + geodeRobots,
      });
    }
  }
  return best;
}

for (const blueprint of parsed) {
  const best = evaluateBlueprint(blueprint, 24);
  answer1 += blueprint.blueprintId * best;
}

console.info(
  `Answer1: ${answer1} after ${(performance.now() - start).toFixed(2)}ms`
);

// ===========================================================
// PART 2
// ===========================================================

let answer2 = 1;

for (let i = 0; i < 3; i++) {
  const best = evaluateBlueprint(parsed[i], 32);
  answer2 *= best;
}

console.info(
  `Answer2: ${answer2} after ${(performance.now() - start).toFixed(2)}ms`
);
