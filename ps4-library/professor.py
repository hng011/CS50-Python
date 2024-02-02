import random

def main() -> any:
    score, counter, level = 0, 0, get_level()    

    for _ in range(10):
        x,y = generate_integer(level)
        ans = x + y

        while True:
            if counter == 3:
                print(f"{x} + {y} = {ans}")
                counter = 0
                break
            
            try:
                usr_inp = int(input(f"{x} + {y} = "))
                if usr_inp == ans:
                    score += 1
                    break
                else:
                    print("EEE")
                    counter += 1
            except ValueError:
                pass

    print("Score:",score)

def get_level() -> int:
    level = 0
    while level <= 0 or level > 3:
        try:
            level = int(input("Level: "))
            if level not in range(1,4):
                raise ValueError
        except ValueError:
            print("Input Number between 1 - 3")

    return level


def generate_integer(level: int) -> tuple:
    def random_int():
        return random.randint(0 if level == 1 else 10**(level-1) , (10**level) - 1)

    return (random_int(), random_int())

if __name__ == "__main__":
    main()