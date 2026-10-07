import json
from pathlib import Path

results = json.loads(Path("results.json").read_text(encoding="utf-8"))

t3 = results["pr_auc"]["t_plus_3m"]
t15 = results["pr_auc"]["t_plus_15m"]
wf = results["walk_forward"]

print("500-mint cohort evaluation")
print(f"T+3m delta:  {t3['baseline_plus_cohorts'] - t3['baseline']:+.3f}")
print(f"T+15m delta: {t15['baseline_plus_cohorts'] - t15['baseline']:+.3f}")
print(f"Walk-forward folds improved: {wf['folds_improved']}/{wf['folds_total']}")
print(f"Walk-forward median delta: {wf['median_delta']:+.3f}")

assert round(t3["baseline_plus_cohorts"] - t3["baseline"], 3) == 0.003
assert round(t15["baseline_plus_cohorts"] - t15["baseline"], 3) == -0.020
assert wf["folds_improved"] == 6
assert wf["folds_total"] == 20
assert wf["median_delta"] == -0.045

print("Summary checks passed.")
