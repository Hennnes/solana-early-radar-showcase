# ANSEM case study — condensed public version

Canonical mint:
`9cRCn9rGT8V2imeM2BaKs13yhMEais3ruM3rPvTGpump`

Launch:
`2026-06-16T21:05:48Z` — slot `426930467`

The underlying case-study dataset covered 20,876 successful mint-address
transactions through T+24h.

## Temporal snapshots

| Cutoff | Successful txs | Conservative unique buyers | Repeated funders |
|---|---:|---:|---:|
| T+1m | 1,050 | 275 | 27 |
| T+5m | 3,349 | 698 | 51 |
| T+15m | 5,565 | 898 | 61 |
| T+30m | 6,390 | 1,021 | 68 |
| T+60m | 7,397 | 1,166 | 76 |
| T+24h | 20,876 | 2,247 | 76 |

The first 60 minutes contained 1,166 meaningful buyers in the research
definition.

## Leakage guard

Every early snapshot was recomputed using only events at or before its cutoff.
Later survival, holder expansion and other outcome fields were not allowed into
the cutoff features.

## Diagnostics considered

The analysis included:

- conservative buy/sell candidates;
- early-wallet history;
- repeated initial funders;
- transaction burstiness;
- same-slot buyer counts;
- holder concentration after heuristic pool/program exclusions;
- dust-like activity;
- prior wallet relationships.

These were treated as diagnostics, not as proof of common control or insider
activity.

## Why the case study was not enough

The token was a known historical case. It could show what might have been
observable early, but it could not validate a predictive model by itself.

That is why the project moved from a single case, to a 75-mint pilot, and then
to the 500-mint temporal evaluation described in `methodology.md`.
