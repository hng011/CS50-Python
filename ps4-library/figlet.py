import sys
from pyfiglet import Figlet

def to_figlet() -> any:
    fig = Figlet()

    try:
        if len(sys.argv) == 1:
            x = input("Input: ")
            return fig.renderText(x)
        else:
            if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                fig.setFont(font=sys.argv[2])
                x = input("Input: ")
                return fig.renderText(x)
            else:
                sys.exit("Invalid usage")
    except:
        sys.exit("Invalid usage")
        
print("Output:\n"+to_figlet())