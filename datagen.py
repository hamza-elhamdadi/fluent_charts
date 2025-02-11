from numpy import random
import json

n = 100
groups = [{"name": "A", "mean": 1}, {"name": "B", "mean": 3}]
data ={"nodes": []}

for i, g in enumerate(groups, 1):
    points = random.normal(loc=g["mean"], scale=0.3, size=(n,))
    for j, p in enumerate(points, 1):
        data["nodes"].append({"group": g["name"], "index": i*j})

with open("data/al.json", "w") as file:
    json.dump(data, file, indent=4)