quiz = {
"What is the smallest Even Number ? " : "2",
"Name the Largest Mammal on Earth ? " : "blue whale",
"What are the Four Magical Letters ? " : "love" 
}

def start(trivia):
    score = 0
    total = 3
    Q = 1
    print("Your Trivia Quiz Starts Now !\n")
    for i in trivia:
        print(f"Q{Q}. {i}")
        ans = (input("Your Answers: ").lower()).strip()
        if(ans==trivia[i]):
            print("Correct ✅\n")
            score +=1;
        else:
            print(f"❌ Wrong the correct answer was {trivia[i]} \n")
        Q+=1;

    print(f"🏆 Your Final Score is {score}/{total} 🌟")

start(quiz)
