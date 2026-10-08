
import sys


if len(sys.argv) != 2:
    sys.exit()

if not sys.argv[1].endswith(".py"):
    sys.exit()

try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit()

count = 0

for line in lines:
    if line.strip() == "":
        continue

    if line.lstrip().startswith("#"):
        continue

    count += 1

print(count)
