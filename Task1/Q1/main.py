import time
import os

def display_gear(n):
    gears = {
        0: [
            "####",
            "#  #",
            "#  #",
            "#  #",
            "####"
        ],
        1: [
            "   #",
            "  ##",
            "   #",
            "   #",
            "   #"
        ],
        2: [
            "####",
            "   #",
            "####",
            "#   ",
            "####"
        ],
        3: [
            "####",
            "   #",
            "####",
            "   #",
            "####"
        ],
        4: [
            "#  #",
            "#  #",
            "####",
            "   #",
            "   #"
        ],
        5: [
            "####",
            "#   ",
            "####",
            "   #",
            "####"
        ],
        6: [
            "####",
            "#   ",
            "####",
            "#  #",
            "####"
        ],
        7: [
            "####",
            "   #",
            "  ##",
            "   #",
            "   #"
        ],
        8: [
            "####",
            "#  #",
            "####",
            "#  #",
            "####"
        ]
    }
    
    pattern = gears[n]
    for str in pattern:
        print(str)

    print()
    

"""
    TBH the clearing screen part is with the ai help//
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def shift(g1, g2):
    print(f"shifting from {g1} to {g2}")
    
    display_gear(g1)

    time.sleep(0.5)

    clear_screen()

    display_gear(g2)


if __name__ == "__main__":
    print("Enter gear: ")
    n = int(input())
    if not isinstance(n, int):
        raise ValueError("input gear should be integer!!")
    elif n > 8 or n < 0:
        raise Exception("input gear should be between 0 and 8!!!")  
    else:
        display_gear(n)

        print("Enter 1 if you wanna select a gear to shift otherwise 0: ")
        want = int(input())

        if want:
            print("Enter a gear to shift to: ")
            n2 = int(input())
            shift(n, n2)
        
