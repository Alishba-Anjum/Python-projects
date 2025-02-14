# Mad Libs Game

# Welcome message
print("Welcome to the Mad Libs Game!")
print("Please provide the following details to create your story.")

# Get user inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb ending in -ing: ")
food = input("Enter a type of food: ")
number = input("Enter a number: ")

# Create the story
story = f"""
Once upon a time, there was a person named {name} who lived in {place}.
One day, while walking through the {adjective} forest, they stumbled upon a {animal} that was {verb}.
Surprised, {name} decided to follow the {animal}.
To their amazement, it led them to a magical tree that grew {food}.
{name} picked {number} {food} from the tree and shared them with the {animal}.
From that day forward, {name} and the {animal} became the best of friends and had many adventures together in {place}.
"""

# Display the story
print("\nHere is your Mad Libs story:\n")
print(story)
