import random
import time
dice = [1,2,3,4,5,6]
how = []
print("── ⋆⋅𖤓⋅⋆ ──── ⋆⋅𖤓⋅⋆ ──── ⋆⋅𖤓⋅⋆ ──")
n =int(input("How many Rounds : "))
for i in range(n):
    how.append(random.choice(dice))

target = sum(how)
print(f"Your Target is : {target}")
print(f"Computed Rolls : {how}\n")

how = []
for i in range(n):
    time.sleep(1.5)
    how.append(random.choice(dice))
    print(f"Round {i+1}: Rolled {how[i]} | Total : {sum(how)} ")
    if(sum(how)>=target):
        print(f"\n╰┈➤ You Won You Reached {target} in {i+1} Rounds  ⮜┈╯")
        print(f"Computed Rolls : {how}\n")
        break
else:
    print(f"\n⁀➴ ♡ You Loss You are still {sum(how)} in {i+1} Rounds")
    print(f"Computed Rolls : {how}\n")

