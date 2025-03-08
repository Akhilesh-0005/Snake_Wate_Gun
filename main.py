import random
def game():
    while(True):
        print("Select Your Choice as follows :\n\t1 : SNAKE\n\t2 : WATER\n\t3 : GUN ")
        user=int(input("Enter Your Choice : "))
        if(user==1):
            user="SNAKE"
        elif(user==2):
            user="WATER"
        elif(user==3):
            user="GUN"
        else:
            print("Invalid Option Chosen\n\tTry Again !!!!!!")
            exit()
        choice=["SNAKE","WATER","GUN"]
        computer=random.choice(choice)
        if(computer.lower()==user.lower()):
            print(f"You chose : {user.upper()}\nComputer chose : {computer}\nHence,It's a Tie !!!")
        else:
            if(computer.lower()=="snake" and user.lower()=="water"):
                print(f"You chose : {user.upper()}\nComputer chose : {computer} \n You Lose!!! As Snake poision the Water ")
            elif(computer.lower()=="snake" and user.lower()=="gun"):
                print(f"You chose : {user.upper()}\nComputer chose : {computer} \n You Win!!! As Gun kills the Snake")
            elif(computer.lower()=="water" and user.lower()=="snake"):
                print(f"You chose : {user.upper()}\nComputer chose : {computer} \n You Win!!! As Snake poision the Water")
            elif(computer.lower()=="water" and user.lower()=="gun"):
                print(f"You chose : {user.upper()}\nComputer chose : {computer} \n You Lose!!! As Water rusts the Gun")
            elif(computer.lower()=="gun" and user.lower()=="water"):
                print(f"You chose : {user.upper()}\nComputer chose : {computer} \n You Win!!! As Water rusts the Gun")
            elif(computer.lower()=="gun" and user.lower()=="snake"):
                print(f"You chose : {user.upper()}\nComputer chose : {computer} \n You Lose!!! As the Gun kills the Snake")
        x=input("Do You want to play Again : (Yes / No) : ")
        if(x.lower()=="yes"):
            game()
        else:
            if(x.lower()=="no"):
                exit()
            else:
                exit()
game()