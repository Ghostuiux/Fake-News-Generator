import random
import data


def personalized_headline(filtered_subjects):
    # user inputs (optional)
    subject_input = input("Enter subject (leave empty for random): ").strip()
    action_input = input("Enter action (leave empty for random): ").strip()
    place_input = input("Enter place (leave empty for random): ").strip()

    # subject decision
    if subject_input == "":
        subject = random.choice(filtered_subjects)
    else:
        subject = subject_input

    # action decision
    if action_input == "":
        action = random.choice(data.actions)
    else:
        action = action_input

    # place decision
    if place_input == "":
        place = random.choice(data.places_things)
    else:
        place = place_input

    headline = f"Breaking News: {subject} {action} {place}"
    return headline

    