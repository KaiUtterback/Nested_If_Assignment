# Objective: Practice the use of nested if statements in creating a simple text based adventure game.
# Task 1
print("")

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input ("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")  
elif place == "cave":
    print("You find a hidden treasure")

# Task 2: Expand the game. If the user chooses "cave", ask them if they want to light a torch
# or proceed in the dark.
print(" ")

if place == "cave":
    cave_option_1 = input("do you want to light a torch, or proceed in the dark? ")
    
# Task 3: Default Path (See pass on line 13)

# Question 2: Quick Decisions: The Event Planner:

# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
if attendees > 100: venue = "large hall"
if attendees < 100: venue = "conference room"

# venue = "large hall" if attendees > 100 else "conference room" = venue 
