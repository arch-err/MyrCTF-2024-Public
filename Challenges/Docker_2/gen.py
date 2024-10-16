#!/usr/bin/env python
import os
import string
import random

os.system("yq '.flag' challenge.yaml > flag.txt")
flag = open("flag.txt").read().strip()

layer = 0
files_per_folder = 1000

for i, flag_part in enumerate(flag):
    weights = [1]*len(string.printable)

    weights[string.printable.index(flag_part)] = files_per_folder*0.10

    str_list = random.choices(
            string.printable,
            weights=weights,
            k=files_per_folder
    )

    os.system(f"mkdir -p tmp/{i}")

    for s in str_list:
        with open(f"tmp/{i}/{''.join(random.choices(string.ascii_lowercase, k=5))}", "w") as f:
            f.write(s)


with open("dockerfile", "w") as f:
    f.write("FROM alpine\n")
    f.write("\n")
    for i in range(len(flag)):
        f.write(f"ADD tmp/{i}/ /chal/\n")

    f.write("\n")
    f.write('CMD [ "echo", "can you find the flag in /chal?" ]\n')

os.system("docker build -t docker_2:latest .")
os.system("docker save -o img.tar docker_2:latest")
os.system("rm flag.txt")
os.system("rm -rf tmp/")
