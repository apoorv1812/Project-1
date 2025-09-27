import random
list=["stone","paper","scissors"]
def stone_paper_scissors():
        a=input("Enter your name: ")
        b=input("Enter your name: ")
        player1=(random.choice(list))
        player2=(random.choice(list))
        print(f'{a} chooses {player1}')
        print(f'{b} chooses {player2}')
        if player1==list[0] and player2==list[1]:
            print(f"The game is won by {b}")
            print("The game is over")
        elif player1==list[0] and player2==list[2]:
            print(f"The game is won by {a}")
            print("The game is over")
        elif player1==list[0] and player2==list[0]:
            print("The game is draw") 
            print("The game is over")
        elif player1==list[1] and player2==list[0]:
            print(f"The game is won by {a}")
            print("The game is over")
        elif player1==list[1] and player2==list[1]:
            print("The game is draw")
            print("The game is over")
        elif player1==list[1] and player2==list[2]:
            print(f"The game is won by {b}")
            print("The game is over")
        elif player1==list[2] and player2==list[0]:
            print(f"The game is won by {b}")
            print("The game is over")
        elif player1==list[2] and player2==list[1]:
            print(f"The game is won by {a}")
            print("The game is over")
        elif player1==list[2] and player2==list[2]:
            print("The game is draw")
            print("The game is over")
    
stone_paper_scissors()