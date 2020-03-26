# Object class creation
class obj:
    def __init__(self, object, description, cost):
        self.object = object
        self.description = description
        self.cost = cost
# Object bank
objects = [
    obj("most costly pen",
        "It contains over 30 carats of De Beer's diamonds on a solid platinum barrel. It has a two-tone, rhodium-treated, 18KT solid gold nib and is personalized with a coat of arms,\n signature or portrait.",
        1470600),
    obj("Eiffel Tower", "It is kinda obvious.", 1287346),
    obj("most costly car", " It is a Bugatti super car.", 19000000),
    obj("Panzer 4", " It was the best German tank in 1947.", 29468),
    obj("Bf-109e", "It was the main propeller fighter aicraft in Nazi Germany.", 2478812),
    obj("most expensive watch", "It is a Rolex that was sold at an auction.", 31000000),
    obj("most expensive toilet", "It is a toilet on the ISS", 19000000),
    obj("most expensive phone", "It is an gold iphone. Yeah, it is going to be expensive.", 48500000),
    obj("the most expensive yacht", "It is made of gold and platinum and is owned by the richest man in Malyasia.", 4800000000),
    obj("the most expensive glasses", "It frickn' swiss and has gold all over.", 400000)
]
# Begining explanation/story creation
start_input = int(input(
    "This is a two-player game where you will take turns guessing the cost of the object/item in USD that the computer will show you and it will also give a description to you."
    "\nPress the number of items you want to have in this game (the maximum is 10) : "))
for obje in objects:
    # Main variable creation
    Player1_score = 0
    Player2_score = 0
    Player1_input = int(input("How much do you think the " + obje.object + " costs, player one? " + obje.description + " Put your answer as an integer: "))
    Player2_input = int(input("How much do you think the " + obje.object + " costs, player two? " + obje.description + " Put your answer as an integer: "))
    if abs(obje.cost - Player1_input) < abs(obje.cost - Player2_input):
        print("You win the first round, player one!")
        Player1_score = Player1_score + 1
        Player2_score = Player2_score
    if abs(obje.cost - Player1_input) > abs(obje.cost - Player2_input):
        print("You win the first round, player two!")
        Player1_score = Player1_score
        Player2_score = Player2_score + 1
    if abs(obje.cost - Player1_input) == abs(objects[0].cost - Player2_input):
        print("It is a tie!")
        Player1_score = Player1_score + 1
        Player2_score = Player2_score + 1

if Player1_score < Player2_score:
    print("You win player two! Congratulations! You got " + str(Player1_score) + " points. Player two, you got " + str(
        Player2_score) + " points.")
elif Player2_score < Player1_score:
    print("You win player two! Congratulations! You got " + str(Player2_score) + " points. Player one, you got " + str(Player1_score) + " points")
elif Player1_score == Player2_score and 0 < Player2_score or 0 < Player1_score:
    print("It is an overall tie! Congratulations to both of you! Both of your scores are five!")
print("The exact answer to the first question was " + str(objects[0].cost) + ". The exact answer to the second question was " + str(objects[1].cost) + ". The exact answer to the third question was " + str(objects[2].cost) + "." + " The exact answer to the fourth question was " + str(objects[3].cost) + "." + " The exact answer to the fifth question was " + str(objects[4].cost) + ".")


