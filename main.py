import data
import random

print("Dear User! Welcome to Fake News Generator.")

inputcat = input("\nWhich category news you want? (Technology/Sports/Politics/Entertainment)").strip()

filtered_subjects = []

for subject in data.subjects:
    cat = data.detectcat(subject)
    if cat.lower() == inputcat.lower():
        filtered_subjects.append(subject)
        
if not filtered_subjects:
    print(f"\nSorry, no subjects found for category '{inputcat}'.")
    print("\nExiting program.")
    exit()

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