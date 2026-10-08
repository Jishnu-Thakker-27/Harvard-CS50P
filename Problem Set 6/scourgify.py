import sys
import csv


if len(sys.argv) != 3:
    sys.exit("Too few or too many command-line arguments")

try:
    with open(sys.argv[1], newline="") as file:
        reader = csv.DictReader(file)

        with open(sys.argv[2], "w", newline="") as output:
            writer = csv.DictWriter(
                output,
                fieldnames=["first", "last", "house"]
            )

            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")

                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")