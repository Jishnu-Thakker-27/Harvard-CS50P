def main():
    names = []

    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            break

    if len(names) == 1:
        result = names[0]
    elif len(names) == 2:
        result = f"{names[0]} and {names[1]}"
    else:
        result = ", ".join(names[:-1]) + f", and {names[-1]}"

    print(f"Adieu, adieu, to {result}")


main()