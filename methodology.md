# Methodology

## Research question

Can recurring early-buying wallet cohorts add useful predictive information
for newly launched Pump.fun tokens beyond a baseline feature set?

## Temporal design

The evaluation used frozen token-cutoff rows. Features for a cutoff were built
only from information available at or before that cutoff.

This is important because later survival, holder growth, market-cap expansion,
attention and other outcome information must not leak into early-time features.

## Development path

### Single-case analysis

The first detailed case study reconstructed the early on-chain state of one
known token and examined:

- launch/lifecycle evidence;
- conservative buyer candidates;
- early-wallet history;
- funding relationships;
- burstiness;
- holder concentration;
- possible coordination diagnostics.

The case study was useful for designing candidate features, but a known winner
cannot establish predictive value on its own.

### Pilot

A 75-mint pilot found recurring wallet pairs and several early cohorts. This
made the cohort hypothesis worth testing on a larger independent sample.

### 500-mint evaluation

The larger evaluation used:

- 500 independent Pump mints;
- 2,500 frozen token-cutoff rows;
- 8,155 unique buyers within 5 minutes;
- 838 buyers with recurring history;
- 2,033 descriptive recurring pairs;
- 33 connected cohorts.

The target's Tier B base rate was 5%.

## Validation result

At the best reported incremental cutoff, T+3m:

- baseline PR-AUC: 0.134;
- baseline + cohort features: 0.137;
- delta: +0.003.

At T+15m:

- baseline PR-AUC: 0.162;
- baseline + cohort features: 0.142;
- delta: -0.020.

Walk-forward validation improved in only 6 of 20 folds, with median delta
-0.045.

## Decision

The cohort hypothesis was not strong enough to justify building a realtime
radar or trading execution layer.

That negative result is the point of the project: the research process
explicitly rejected a promising-looking hypothesis after larger-sample
temporal validation did not support it.

## Limitations

The original analysis also tracked limitations such as:

- conservative buy/sell inference rather than claiming exact swap volume;
- potentially truncated wallet-history pages;
- heuristic pool/custody exclusions;
- common funders being service/exchange/bot infrastructure rather than proof of
  common ownership;
- coordination indicators not being proof of insider control.

## Next research direction

A later direction considered structural pre-launch/funding signals rather than
simple recurring-buyer identity:

- funding ancestry;
- first SOL source;
- fresh-wallet funding;
- funding clusters;
- creator/deployer adjacency;
- coordinated wallet preparation;
- buy-size and timing patterns.

No realtime or trading system is claimed in this repository.
