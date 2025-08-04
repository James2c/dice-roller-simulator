import random

def main():
    while True:
        try:
            sides = int(input("How many sides should the die have? "))
            if sides < 2:
                print("Dice must have at least 2 sides")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue
    
        result = roll_dice(sides)
        print(f"You rolled a {result} on a {sides}-sided die")

        again = input("Would you like to roll again? (y/n):").lower()
        if again == "y":
            continue
        else:
            break


def roll_dice(sides):
    return random.randint(1, sides)


if __name__ == "__main__":
    main()