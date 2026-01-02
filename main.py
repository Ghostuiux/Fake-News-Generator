import data
import random

print("Dear User! Welcome to Fake News Generator.")

while True:
    subject = random.choice(data.subjects)
    action = random.choice(data.actions)
    places_thing = random.choice(data.places_things)
    
    headline = f"Breaking News: {subject} {action} {places_thing}" #f"" used to make a sentence using words.
    print("\n" + headline)
    
    userinput = input("\nDo you want another headline? (Yes/No)").strip() #strip used to remove spaces before after the word just focus on main word.
    if userinput == "No":
        break
    
print("\nThank you so much for using Fake News Headline Generator.")