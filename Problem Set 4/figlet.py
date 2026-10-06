import sys
import random
import pyfiglet


def main():

    if len(sys.argv) == 1:
        font = random.choice(pyfiglet.FigletFont.getFonts())

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

        if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
            sys.exit("Invalid font")

        font = sys.argv[2]

    else:
        sys.exit("Invalid usage")

    text = input("Input: ")

    f = pyfiglet.Figlet(font=font)
    print(f.renderText(text))


main()