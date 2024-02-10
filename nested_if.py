# Objective: Practice the use of nested if statements in creating a simple text based adventure game.
# Task 1
print("")

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input ("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action != "climb a tree":
            print("You found a boat!")  
elif place == "cave":
    print("You find a hidden treasure")
else: 
    pass

# Task 2: Expand the game. If the user chooses "cave", ask them if they want to light a torch
# or proceed in the dark.

if place == "cave":
    cave_option_1 = input("do you want to light a torch, or proceed in the dark? ")
    
# Task 3: Default Path


    