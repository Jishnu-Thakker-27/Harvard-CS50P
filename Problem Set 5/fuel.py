def main():
    fraction = input("Fraction: ")

    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):
        pass


def convert(fraction):
    x, y = fraction.split("/")

    x = int(x)
    y = int(y)

    if x > y:
        raise ValueError

    percentage = round((x / y) * 100)

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()