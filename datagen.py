from numpy import random
import json

n = 100
conditions = [
    {
        "filename": "data/al.json",
        "groups": [{"name": "A", "mean": 1}, {"name": "B", "mean": 3}]
    }
]

for condition in conditions:
    data ={"nodes": []}

    for i, g in enumerate(condition["groups"]):
        points = random.normal(loc=g["mean"], scale=0.3, size=(n,))
        for j, p in enumerate(points, 1):
            data["nodes"].append({"group": g["name"], "value": p, "index": i*n + j})

    with open(condition["filename"], "w") as file:
        json.dump(data, file, indent=4)