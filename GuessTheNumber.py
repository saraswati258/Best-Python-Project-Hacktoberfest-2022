n = 18

for i in range(5,0,-1):
    a = int(input("enter your no. "))
    if a == 18 :
        print("you win ")
        print("GAME OVER")
        break
    else:
        if a<18:
           print("increase your no.")
           print("no. of guesses left ",i-1)
        elif a>18:
            print("decrease your no. ")
            print("no. of guesses left ",i-1)
    
if i ==1:
        print("you loose the game")
else:
        print("no. of guesses left ",i-1)
        #or 
