import random
import time

noun = input("Enter a Noun for your Story: ").lower()
verb = input("Enter a Verb for your Story: ").lower()
place = input("Enter a place for your Story: ").lower()
adjective = input("And Finally Enter an Adjective for your Story: ").lower()

print("Here is Your Story :\n")

def new_story(noun, verb, place, adjective):
    stories = [
    f"One day, a {adjective} {noun} went to the {place}. The {noun} {verb} around the {place} and noticed something unusual. The {adjective} {noun} decided to {verb} closer to it. Suddenly, something unexpected happened, and the {noun} quickly {verb} away. After a moment, the {noun} returned and {verb} again. Everyone in the {place} laughed when they saw the {adjective} {noun} because it {verb} so happily.",

    f"One morning, a {adjective} {noun} arrived at the {place}. The {noun} {verb} across the {place} and saw another interesting {noun}. The {adjective} {noun} wanted to {verb} with it, so they moved closer together. Suddenly, the {noun} fell down, and the {adjective} {noun} {verb} to help. After a few seconds, everything was fine again. People in the {place} smiled at the {adjective} {noun} because it {verb} with great excitement.",

    f"Yesterday, a {adjective} {noun} was walking through the {place}. While the {noun} {verb} around, it discovered a small object on the ground. The {adjective} {noun} picked it up and {verb} toward the other side of the {place}. Suddenly, the object disappeared, so the {noun} {verb} around looking for it. Finally, the {noun} found it and {verb} happily. Everyone at the {place} was surprised to see how the {adjective} {noun} {verb} so confidently.",

    f"One afternoon, a {adjective} {noun} decided to visit the {place}. The {noun} {verb} through the {place} and noticed something moving nearby. Curious about it, the {adjective} {noun} went closer and {verb} carefully. Suddenly, the thing moved away, and the {noun} {verb} after it. After a short while, the {noun} stopped and looked around. Everyone in the {place} smiled at the {adjective} {noun} because it {verb} in such a funny way.",

    f"Once upon a time, a {adjective} {noun} lived near a beautiful {place}. Every day, the {noun} {verb} around the {place} and looked for something interesting. One day, the {adjective} {noun} found a strange object and decided to {verb} it. Suddenly, the object moved, and the {noun} {verb} after it. After searching for a while, the {noun} finally found it again. The people in the {place} were happy to see the {adjective} {noun} because it {verb} with great energy."
    ]
    story = random.choice(stories)
    time.sleep(1)
    print(story)

if __name__ == "__main__":
        new_story(noun, verb, place, adjective)