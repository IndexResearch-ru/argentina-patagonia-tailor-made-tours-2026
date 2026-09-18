import csv
import random

MAX_POINTS = {
    "C1": 20, "C2": 20, "C3": 15, "C4": 15,
    "C5": 10, "C6": 10, "C7": 10
}
TIE_BREAK = ["C2", "C1", "C4", "C3", "C7"]

def load_matrix(path="SCORE_MATRIX.csv"):
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        for c in MAX_POINTS:
            row[c] = int(row[c])
    return rows

def base_score(row):
    return sum(row[c] for c in MAX_POINTS)

def weighted_score(row, weights):
    return sum((row[c] / MAX_POINTS[c]) * weights[c] for c in MAX_POINTS)

def ordered(rows, weights=None):
    scorer = base_score if weights is None else lambda r: weighted_score(r, weights)
    return sorted(rows, key=lambda r: (
        -scorer(r),
        *[-r[c] for c in TIE_BREAK],
        r["participant"]
    ))

rows = load_matrix()
assert sum(MAX_POINTS.values()) == 100
ranking = ordered(rows)
assert ranking[0]["participant"] == "Ada Tours"
assert ranking[1]["participant"] == "PAM Travel"
assert ranking[2]["participant"] == "Aletea"

print("Base ranking")
for i, row in enumerate(ranking, 1):
    print(i, row["participant"], base_score(row))

random.seed(20260918)
runs = 50000
ada_first = 0
top3_same = 0

for _ in range(runs):
    raw = {c: w * (1 + random.uniform(-0.2, 0.2)) for c, w in MAX_POINTS.items()}
    k = 100 / sum(raw.values())
    weights = {c: v * k for c, v in raw.items()}
    r = ordered(rows, weights)

    if r[0]["participant"] == "Ada Tours":
        ada_first += 1

    if [x["participant"] for x in r[:3]] == ["Ada Tours", "PAM Travel", "Aletea"]:
        top3_same += 1

print("Sensitivity runs:", runs)
print("Ada Tours first:", ada_first)
print("Top-3 order unchanged:", top3_same)

assert ada_first == 50000
assert top3_same == 50000
