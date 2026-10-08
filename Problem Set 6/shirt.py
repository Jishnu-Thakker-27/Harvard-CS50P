import sys
from PIL import Image, ImageOps


if len(sys.argv) != 3:
    sys.exit("Too few or too many command-line arguments")



input_extension = sys.argv[1].lower().split(".")[-1]
output_extension = sys.argv[2].lower().split(".")[-1]

valid_extensions = ["jpg", "jpeg", "png"]



if input_extension not in valid_extensions or output_extension not in valid_extensions:
    sys.exit("Invalid output")



if input_extension != output_extension:
    sys.exit("Input and output have different extensions")


try:
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")



shirt = Image.open("shirt.png")



image = ImageOps.fit(image, shirt.size)



image.paste(shirt, (0, 0), shirt)



image.save(sys.argv[2])