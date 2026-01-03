import data
import category
import userinput
import random

print("Dear User! Welcome to Fake News Generator.")

inputcat = input("\nWhich category news you want? (Technology/Sports/Politics/Entertainment)").strip()

filtered_subjects = []

for subject in data.subjects:
    cat = category.detectcategory(subject)
    if cat.lower() == inputcat.lower(): ##lower here represent if we write key word in small or capital letter it can easily compare that except case sensitivity.
        filtered_subjects.append(subject)
        
if not filtered_subjects:
    print(f"\nSorry, no subjects found for category '{inputcat}'.")
    print("\nExiting program.")
    exit()

while True:
    choice = input("\nChoose Mode: \n1=Random Headline \n2=Personalized Headline \nEntre choice: ").strip()
    if choice == "1":
        subject = random.choice(filtered_subjects)
        action = random.choice(data.actions)
        places_thing = random.choice(data.places_things)
        
        headline = f"Breaking News: {subject} {action} {places_thing}" #f"" used to make a sentence using words.
        print("\n" + headline)
    
    elif choice == "2":
        headline = userinput.personalized_headline(filtered_subjects)
        print("\n" + headline)
        
    else:
        print("\nInvalid choice. Please select 1 or 2.")
        continue
           
    anotherheadline = input("\nDo you want another headline? (Yes/No)").strip() #strip used to remove spaces before after the word just focus on main word.
    if anotherheadline == "No":
        break
    
print("\nThank you so much for using Fake News Headline Generator.")