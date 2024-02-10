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
    
# Task 3: Default Path (See pass on line 16)

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
    
# In my head, the large hall would just come loaded with these options
    
if venue == "conference room":
    if attendees >= 30 < 60:
        print("You should consider adding an audio system to your package")
    elif attendees >= 60:
        print("You should consider adding an audio system and projector to your package")
    elif attendees < 30:
        print("You do not need a projector or audio system unless you would like one.")
        
# Task 3: catering choices: Ask the user if they want vegetarian food. 
# Reccomend veggie delight caterers if yes, otherwise reccomend gourmet meals caterers
print(" ")

meal = input("Would you like vegetarian food to be served at your event? Yes or No: ")     

if meal == "Yes":
    print("We reccomend Veggie Delight Caterers for your event")
else:
    print("We reccomend Gourmet Meals Caterers for your event")
    
# Question 3: Silent Error handler
print(" ")

# Task 1 Code Correction:

try:
    x = 1 / 0
except ZeroDivisionError:
    pass

# Task 2: Division calculator
B = "two"
try: 
    A = 3 / B
except TypeError:
    pass

# Task 3: File Reader

try:
    filename = input("Enter the filename to read: ")
    with open(filename, 'r') as file:
        file_contents = file.read()
        
        print("Contents of the file:")
        print(file_contents)
except FileNotFoundError:
    pass

# Question 4: Nested Quick Decisions: Shopping Assistant:
print(" ")

# Task 1 Code Correction

weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater" if weather == "cold" else "you made an incorrect entry" # I added this last else statement because I felt we needed a catch all if weather == something other than sunny, rainy, cold.
print(clothing)

# Task 2: Extra Clothing Reccomendations:

print("Here are some extra clothing items you may consider adding to your outfit:")

extra = "shorts and a T shirt" if weather == "sunny" else "rain coat and boots" if weather == "rainy" else "hat and boots" if weather == "cold" else "you made an incorrect entry"
print(extra)

# Task 3: Accessories:

print("Here are some accessories you may want to include in your option:")
