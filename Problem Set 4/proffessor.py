import random


def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y
        attempts = 0

        while attempts < 3:
            try:
                guess = int(input(f"{x} + {y} = "))

                if guess == answer:
                    score += 1
                    break
                else:
                    print("EEE")

            except ValueError:
                print("EEE")

            attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()