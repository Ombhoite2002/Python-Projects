import random
def Rock_Paper_Scissors(player1 , player2):
    winner = True
    if(player1 == 'r' and player2 == 2):
        print("Player1 = Rock\n Player2 = Paper")
        winner = False
    elif(player1 == 'p' and player2 == 1):
        print("Player1 = Paper\n Player2 = Rock")
        winner = True
    elif(player1 == 'p' and player2 == 3):
        print("Player1 = Paper\n Player2 = Scissors")
        winner = False
    elif(player1 == "s" and player2 == 2):
        print("Player1 = Scissors\n Player2 = Paper")
        winner = True
    elif(player1 == 's' and player2 == 1):
        print("Player1 = Scissors\n Player2 = Rock")
        winner = False
    elif(player1 == 'r' and player2 == 3):
        print("Player1 = Rock\n Player2 = Scissors")
        winner = True
    else:
        print("This round is tie.")
        winner = None
    return winner
choice = True
player1_points = 0
player2_points = 0
while choice:
    print("\n*****************Rock Paper Scissors**********************\n")
    for i in range(3):
        player1 = input("Enter the 'r' for Rock 'p' for Paper and 's' for scissors: ")
        player2 = random.randint(1,3) # Here the value 1 2 and 3 represents the Rock Paper and Scissors
        result = Rock_Paper_Scissors(player1,player2)
        
        if result:
            player1_points = player1_points + 1
        elif result is False:
            player2_points = player2_points + 1
        elif result is None:
            player1_points = player1_points
            player2_points = player2_points   
        
    if player1_points > player2_points:
        print(f"The winner is Player 1. points = {player1_points}")
    elif player2_points > player1_points:
        print(f"The winner is player 2. points = {player2_points}")
    elif player1_points == player2_points:
        print(f"This round is Tie because points are equal.player1 points = {player1_points} and player2 points = {player2_points}")
    player1_points = 0
    player2_points = 0
    choice = input("do you want to continue if yes then click 'y' if No then click 'n': ")
    if(choice == 'y'):
        continue
    else:
        break

        
        