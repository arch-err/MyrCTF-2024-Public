import collections
import json
import os

# extract layer order from manifest
with open("out/manifest.json") as f:
    manifest = json.load(f)

layers = manifest[0]["Layers"]

os.system("rm -rf tmp")
os.system("mkdir -p tmp")

flag = ""

for layer_path in layers[1:]:
    print("Checking layer", layer_path)
    layer_path: str
    name = layer_path.split("/")[-1]

    os.system(f"cp out/{layer_path} tmp/")
    os.system(f"mkdir tmp/{name}.d")
    os.system(f"tar xf tmp/{name} -C tmp/{name}.d/")

    flag_things = []

    for file in os.listdir(f"tmp/{name}.d/chal/"):
        with open(f"tmp/{name}.d/chal/{file}") as f:
            flag_things.append(f.read())
    flag += collections.Counter(flag_things).most_common()[0][0]

os.system("rm -rf tmp")
print(flag)