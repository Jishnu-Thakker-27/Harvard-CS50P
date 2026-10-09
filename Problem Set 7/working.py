
import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.fullmatch(pattern, s)

    if not match:
        raise ValueError

    h1, m1, ap1, h2, m2, ap2 = match.groups()

    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1) if m1 is not None else 0
    m2 = int(m2) if m2 is not None else 0

    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError

    if not (0 <= m1 <= 59 and 0 <= m2 <= 59):
        raise ValueError

    if ap1 == "AM":
        h1 = 0 if h1 == 12 else h1
    else:
        h1 = 12 if h1 == 12 else h1 + 12

    if ap2 == "AM":
        h2 = 0 if h2 == 12 else h2
    else:
        h2 = 12 if h2 == 12 else h2 + 12

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()
