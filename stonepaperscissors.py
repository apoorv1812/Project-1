def stone_paper_scissors():
    a=input("Enter your name: ")
    b=input("Enter your name: ")
    player1=(input("Choose from stone,paper and scissors: ")) 
    player2=(input("Choose from stone,paper and scissors: ")) 
    if player1=="stone" and player2=="paper":
        print(f"The game is won by {b}")
        print("The game is over")
    elif player1=="stone" and player2=="scissors":
        print(f"The game is won by {a}")
        print("The game is over")
    elif player1=="stone" and player2=="stone":
        print("The game is draw") 
        print("The game is over")
    elif player1=="paper" and player2=="stone":
        print(f"The game is won by {a}")
        print("The game is over")
    elif player1=="paper" and player2=="paper":
        print("The game is draw")
        print("The game is over")
    elif player1=="paper" and player2=="scissors":
        print(f"The game is won by {b}")
        print("The game is over")
    elif player1=="scissors" and player2=="stone":
        print(f"The game is won by {b}")
        print("The game is over")
    elif player1=="scissors" and player2=="paper":
        print(f"The game is won by {a}")
        print("The game is over")
    elif player1=="scissors" and player2=="scissors":
        print("The game is draw")
        print("The game is over")
    

stone_paper_scissors()