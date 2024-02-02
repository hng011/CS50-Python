import sys
from PIL import Image, ImageOps

def get_arg() -> tuple:
   
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    ext_arg1 = sys.argv[1].split(".")[1].lower()
    ext_arg2 = sys.argv[2].split(".")[1].lower()
    
    if ext_arg2 not in ["png", "jpg", "jpeg"]:
        sys.exit("Invalid output")
    elif ext_arg1 != ext_arg2:
        sys.exit("Input and output have different extensions")
    else:
        return (sys.argv[1], sys.argv[2])
    
def combine_img(first_arg:str, second_arg) -> Image:
    try:
        shirt = Image.open("shirt.png")
        im = Image.open(first_arg)
        resized = ImageOps.fit(im, shirt.size)
        resized.paste(shirt, box=None, mask=shirt)
        resized.save(second_arg)

    except FileNotFoundError:
        sys.exit("Input does not exist")

    except Exception as e:
        sys.exit(e)

def main():
    input_file = get_arg()[0]
    output_file = get_arg()[1] 
    
    # combine and save
    combine_img(input_file, output_file)

main()