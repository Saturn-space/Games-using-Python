import random

words = ["Television","Cinderella","Friendship","Everything"]
word = random.choice(words)

attempts = 7
guessed = set()
print("Guess The Word !")
while attempts>0:
    display = " ".join(c if c in guessed else "_" for c in word)
    print(f"\nword: {display} \nAttempts left : {attempts}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You Already Guessed that Letter")
        continue
    guessed.add(guess)

    if guess not in word:
        attempts -=1
        print("Wrong Guess !")

    if all(c in guessed for c in word):
        print(f"\n You Win! the Word was {word}")
        break

else:
    print(f"Out of Attempts the Word was{word}")

