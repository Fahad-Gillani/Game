import random
words=["hello","garden","sky"]
name=input("Please Enter Your Name : ")
word=random.choice(words)
print(f"Welcome {name}!\nGuess the word To Win Game")
turns=10
print("Guess the Character")
guess=''
while(turns>0):
     
    for option in word:
        fail=0
        if option in guess:
            print(option,end=" ")
        else: 
         print("____")
         fail+=1

    if fail== 0:
        print("You Win!")
        print(f"The Word is : {word}" )
        break
   
    print()
    option=input("Guess a Character : ")
    guess+=option

    if option not in word:

        turns-=1
        print("Wrong Guess")
        print(f"You Have {turns} left Only  ")

    
    if turns ==  0:
        print("You Loose!")        
        
