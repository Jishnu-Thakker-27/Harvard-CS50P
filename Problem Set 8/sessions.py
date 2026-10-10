
from datetime import date
import sys
import inflect


def main():
    birth_date = input("Date of Birth: ")

    try:
        parsed_date = date.fromisoformat(birth_date)

        if parsed_date.isoformat() != birth_date:
            sys.exit("Invalid date")

    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    minutes = minutes_since_birth(parsed_date, today)

    if minutes < 0:
        sys.exit("Invalid date")

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")


def minutes_since_birth(birth_date, today):
    return (today - birth_date).days * 24 * 60


if __name__ == "__main__":
    main()
