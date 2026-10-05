months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            date = input("Date: ")

            # Format: MM/DD/YYYY
            if "/" in date:
                month, day, year = date.split("/")

                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

            # Format: Month DD, YYYY
            elif "," in date:
                month, day_year = date.split(" ", 1)
                day, year = day_year.split(",")

                day = int(day)
                year = int(year)

                if month in months and 1 <= day <= 31:
                    month = months.index(month) + 1
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

        except (ValueError, IndexError):
            pass


main()