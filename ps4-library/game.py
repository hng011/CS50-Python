import random, sys

def set_level() -> int:
    level = 0
    while level <= 0:
        try:
            level = int(input("Level: "))            
        except ValueError:
            print("Input Number!!!")
    
    return level+1
    
def main() -> any:
    guess = None
    ans = random.randint(1, set_level())
    while guess != ans:
        try:
            guess = int(input("Guess: "))
            if(guess < ans):
                print("Too small!")
            if(guess > ans):
                print("Too large!")
        except ValueError:
            print("Input Number!!!")

    sys.exit("Just right!")

main()