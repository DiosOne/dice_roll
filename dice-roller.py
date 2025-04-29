import random

print("Welcome to the Dice Roll Simulator!")

# Prompt the user to select a dice type
print("Select a dice to roll: d4, d6, d8, d10, d12, d20, or percentile (d100)")
dice_type = input("Enter your choice (e.g., d6): ").strip().lower()

# Determine the maximum number based on the dice type
if dice_type == "d4":
    max_number = 4
elif dice_type == "d6":
    max_number = 6
elif dice_type == "d8":
    max_number = 8
elif dice_type == "d10":
    max_number = 10
elif dice_type == "d12":
    max_number = 12
elif dice_type == "d20":
    max_number = 20
elif dice_type == "d100" or dice_type == "percentile":
    max_number = 100
else:
    print("Invalid dice type. Please restart the program and try again.")
    exit()

# Roll the dice and display the result
random_number = random.randint(1, max_number)
print(f"You rolled a {dice_type}: {random_number}")
