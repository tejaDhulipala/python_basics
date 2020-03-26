# Object class creation
class obj:
    def __init__(self, object, description, cost):
        self.object = object
        self.description = description
        self.cost = cost


# Object bank
objects = [
    obj("most costly pen",
        "contains over 30 carats of De Beer's diamonds on a solid platinum barrel. It has a two-tone, rhodium-treated, 18KT solid gold nib and is personalized with a coat of arms,\n signature or portrait.",
        1470600),
    obj("eiffel tower", " Kinda obvious", 1287346),
    obj("most costly car", " A Bugatti supercar", 19000000),
    obj("Panzer 4", "the best German tank in 1947", 29468),
    obj("Bf-109e", "It was the main propeller fighter aicraft in Nazi Germany.", 2478812)
]
# Main variable creation
Player1_score = 0
Player2_score = 0
# Begining explanation/story creation
start_input = (str(input(
    "This is a two-player game where you will take turns guessing the cost of the object/item in USD that the computer will show you and it will also give a description to you."
    "\nPress lowercase 'a' to continue. ")))
# Game is starting
if start_input == "a":
    #              The first question
    Player1_guess1 = int(input(
        "How much do you think the world's costliest pen costs, player 1? It contains contains over 30 carats of De Beers diamonds on a solid platinum barrel. Put your answer as an integer: "))
    Player2_guess1 = int(input(
        "How much do you think the world's costliest pen costs, player 2? It contains contains over 30 carats of De Beers diamonds on a solid platinum barrel. Put your answer as an integer:  "))
    if abs(objects[0].cost - Player1_guess1) < abs(objects[0].cost - Player2_guess1):
        print("You win the first round, player one!")
        Player1_score = Player1_score + 1
        Player2_score = Player2_score
    elif abs(objects[0].cost - Player2_guess1) < abs(objects[0].cost - Player1_guess1):
        print("You win the first round, player two!")
        Player1_score = Player1_score
        Player2_score = Player2_score + 1
    else:
        print("It is a tie!")
        Player1_score = Player1_score + 1
        Player2_score = Player2_score + 1
    #              Movement to the second question. The if statement will always be satisfied and is just a barrier to the next part of the game
    if 0 < Player2_score or 0 < Player1_score or Player1_score == Player2_score:
        Player1_guess2 = int(input(
            "How much money do you think it went into the construction the Eiffel Tower, player 1? It is the famous tower in Paris that is very tall. Put you answer as an integer: "))
        Player2_guess2 = int(input(
            "How much money do you think it went into the construction the Eiffel Tower, player 2? It is the famous tower in Paris that is very tall. Put you answer as an integer: "))
        if abs(objects[1].cost - Player1_guess2) < abs(objects[1].cost - Player2_guess2):
            print("You win the second round, player one!")
            Player1_score = Player1_score + 1
            Player2_score = Player2_score
        elif abs(objects[1].cost - Player2_guess2) < abs(objects[1].cost - Player1_guess2):
            print("You win the second round, player two!")
            Player1_score = Player1_score
            Player2_score = Player2_score + 1
        else:
            print("It is a tie")
            Player1_score = Player1_score + 1
            Player2_score = Player2_score + 1
            # Movement to the thid question
        if 1 < Player2_score or 1 < Player1_score or Player1_score == Player2_score:
            Player1_guess3 = int(input(
                "How much do you think the world's most expensive car costs, player one? It is " + objects[
                    2].description + " . Put your answer as an integer: "))
            Player2_guess3 = int(input(
                "How much do you think the world's most expensive car costs, player two? It is " + objects[
                    2].description + " . Put your answer as an integer: "))
            if abs(objects[2].cost - Player1_guess3) < abs(objects[2].cost - Player2_guess3):
                print("You win the third round, player one!")
                Player1_score = Player1_score + 1
                Player2_score = Player2_score
            elif abs(objects[2].cost - Player2_guess3) < abs(objects[2].cost - Player1_guess3):
                print("You win the third round, player two!")
                Player1_score = Player1_score
                Player2_score = Player2_score + 1
            else:
                print("It is a tie!")
                Player1_score = Player1_score + 1
                Player2_score = Player2_score + 1
            if 2 < Player1_score or 2 < Player2_score or Player2_score == Player1_score:
                Player1_guess4 = int(input(
                    "Now it is time for the part of the game I like to call, The Price is Reich! I will ask you about how much Nazi war weapons cost adjusted to today's USD.\n First off, how much did a Panzer 4 cost in 1947, player one? It was " +
                    objects[3].description + ". Put your answer as an integer: "))
                Player2_guess4 = int(input(
                    "Now it is time for the part of the game I like to call, The Price is Reich! I will ask you about how much Nazi war weapons cost adjusted to today's USD.\n First off, how much did a Panzer 4 cost in 1947, player two? It was " +
                    objects[3].description + ". Put your answer as an integer: "))
                if abs(objects[3].cost - Player1_guess4) < abs(objects[3].cost - Player2_guess4):
                    print("You win the fourth round, player one!")
                    Player1_score = Player1_score + 1
                    Player2_score = Player2_score
                elif abs(objects[3].cost - Player2_guess4) < abs(objects[3].cost - Player1_guess4):
                    print("You win the fourth round, player two!")
                    Player1_score = Player1_score
                    Player2_score = Player2_score + 1
                else:
                    print("It is a tie!")
                    Player1_score = Player1_score + 1
                    Player2_score = Player2_score + 1
                if 3 < Player1_score or 3 < Player2_score or Player2_score == Player1_score:
                    Player1_guess5 = int(input(
                        "Next up on The Price is Riech, guess the cost of making a single Bf-109e. " + objects[
                            4].description + " Put your answer as an integer: "))
                    Player2_guess5 = int(input(
                        "Next up on The Price is Riech, guess the cost of making a single Bf-109e. " + objects[
                            4].description + " Put your answer as an integer: "))
                    if abs(objects[4].cost - Player1_guess5) < abs(objects[4].cost - Player2_guess5):
                        print("You win the fifth round, player one!")
                        Player1_score = Player1_score + 1
                        Player2_score = Player2_score
                    elif abs(objects[4].cost - Player2_guess5) < abs(objects[4].cost - Player1_guess5):
                        print("You win the fifth round, player one!")
                        Player1_score = Player1_score
                        Player2_score = Player2_score + 1
                    else:
                        print("It is a tie!")
                        Player1_score = Player1_score + 1
                        Player2_score = Player2_score + 1
    # Final tallying
if Player2_score < Player1_score:
    print("You win player one! Congratulations! You got " + str(Player1_score) + " points. Player two, you got " + str(Player2_score) + " points.")
elif Player1_score < Player2_score:
    print("You win player two! Congratulations! You got " + str(Player2_score) + " points. Player one, you got " + str(Player1_score) + " points.")
elif Player1_score == Player2_score and 0 < Player2_score or 0 < Player1_score:
    print("It is an overall tie! Congratulations to both of you! Both of your scores are five!")
print("The exact answer to the first question was " + str(objects[0].cost) + ". The exact answer to the second question was " + str(objects[1].cost) + ". The exact answer to the third question was " + str(objects[2].cost) + "." + " The exact answer to the fourth question was " + str(objects[3].cost) + "." + " The exact answer to the fifth question was " + str(objects[4].cost) + ".")
