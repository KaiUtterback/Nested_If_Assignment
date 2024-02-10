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
else: 
    pass

# Task 2: Expand the game. If the user chooses "cave", ask them if they want to light a torch
# or proceed in the dark.
print(" ")

if place == "cave":
    cave_option_1 = input("do you want to light a torch, or proceed in the dark? ")
    
# Task 3: Default Path (See pass on line 13)

# Question 2: Quick Decisions: The Event Planner:

# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
if attendees >= 100: venue = "large hall"
else: venue = "conference room"
print(venue)

# Task 2: Venue Selection: Enhance the program to reccomend additional facilities like 
# audio system or projector based on number of attendees.

if venue == "large hall":
    print("Both a projector and audio system are included in this package")
if venue == "conference room":
    if attendees >= 30 < 60:
        print("You should consider adding an audio system to your package")
    elif attendees >= 60:
        print("You should consider adding an audio system and projector to your package")