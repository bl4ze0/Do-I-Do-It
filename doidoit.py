import random

print("Welcome to Do I Do It")
print("This is a code that chooses if you do it or not!")
print("By: AgueroCn\n")

choicemaker = ["Do it", "Don't Do It", "Definitly not", "Why not"]
choices = ["q", "s", "S", "Q"]
playchoices = ["S", "s"]
endchoices = ["Q", "q"]


while True:
    user_input = input("\n-To starts choosing [S]\n-To leave [Q]\n\nYour choice: ")
    
    if user_input in endchoices:
        print("Bye!")
        break      
        
    if user_input in playchoices:
        value = random.choice(choicemaker)
        print(value)
        continue
    else:
        print("Not a valid option! Try again")
        continue

    
    
    


        
    


