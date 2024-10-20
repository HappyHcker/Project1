import random ##Importing module random for dice roll

##making codes that will roll dice
def rolling_dice():
     return random.randint(1,6)

##main code that will get used after asking the players and also use the code that will roll dice
def main(Total_Players_List, rounds):
    score_system = {}

    for player in Total_Players_List:
        score_system[player] = 0

    for round_number in range(1, rounds+1):
        print("\nRound" + str(round_number))

        for player in Total_Players_List:
            input(player + ", Press Enter to Roll the Dice!")
            dice_result = rolling_dice()
            print(player + " rolled a " + str(dice_result))
            score_system[player] += dice_result

    ranking_players = list(score_system.keys())
    ranking_players.sort(key=lambda player: score_system[player], reverse=True)

    print("\nFinal Scores:")
    for player in ranking_players:
        print(player + ": " + str(score_system[player]))

    print("\nRanking:")
    for rank in range(len(ranking_players)):
        player = ranking_players[rank]
        print("Rank "+ str(rank + 1) + ": " + player)


##Below code use try because in bottom except ValueError is used.
try:
    Total_Players = int(input("How many people are playing the Game?: "))

    if Total_Players > 8:
        print("Sorry, " + str(Total_Players) + " people exceed the maximum number of players that can play. Maximum: 8 players")
    elif Total_Players <= 0:
        print("Sorry, less than 0 players can not play the game.")
    else:
        print("Good! We have a total of " + str(Total_Players) + " playing!")

        Total_Players_List = []

        for i in range(Total_Players):
            Player_Name = input(f"{i+1} Player: ")
            Total_Players_List.append(Player_Name)

        print("These players are joining the Game!: " + str(Total_Players_List))

        rounds = int(input("How many rounds should we play?: "))
        
        print("\nThanks for Joining the Game! Lets Start the Game!\n")
        main(Total_Players_List, rounds)
        


##During the input Total_players if the value turns out to be invalid it will print the statement
except ValueError: 
    print("Please Enter a Valid Number! ⚠️") 
