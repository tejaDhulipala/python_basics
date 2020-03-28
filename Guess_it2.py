import random
# Object class creation
class obj:
    def __init__(self, object, description, cost):
        self.object = object
        self.description = description
        self.cost = cost


# Object bank
objects = [
    obj("most costly pen",
        "It contains over 30 carats of De Beer's diamonds on a solid platinum barrel. It has a two-tone, "
        "rhodium-treated, 18KT solid gold nib and is personalized with a coat of arms,\n signature or portrait.",
        1470600),
    obj("most expensive shoes", "It is a women's shoe with diamonds and gold all over.", 17000000),
    obj("most costly car", " It is a Bugatti super car.", 19000000),
    obj("Panzer 4", " It was the best German tank in 1947.", 29468),
    obj("Bf-109e", "It was the main propeller fighter aircraft in Nazi Germany.", 2478812),
    obj("most expensive watch", "It is a Rolex that was sold at an auction.", 31000000),
    obj("most expensive toilet", "It is a toilet on the ISS", 19000000),
    obj("most expensive phone", "It is an gold iphone. Yeah, it is going to be expensive.", 48500000),
    obj("the most expensive yacht", "It is made of gold and platinum and is owned by the richest man in Malyasia.", 4800000000),
    obj("the most expensive glasses", "It's swiss and has gold all over.", 400000),
    obj("most expensive jeans", "It is made of crystals.", 10000)
]
random.shuffle(objects)
# Begining explanation/story creation
start_input = input(
    "This is a two-player game where you will take turns guessing the cost of the object/item in USD that the "
    "computer will show you and it will also give a description to you. "
    "\nPress the number of items you want to have in this game (the maximum is " + str(len(objects)) + ") : ")

while not start_input.isnumeric() or int(start_input) > len(objects):
    start_input = input("please enter a single number between 1 and " + str(len(objects)) + ": ")
start_input = int(start_input)

i = 0
Player1_score = 0
Player2_score = 0
while i < start_input:
    # Main variable creation
    Player1_input = input("How much do you think the " + objects[i].object + " costs, player one? " + objects[i].description + " Put your answer as an integer: ")
    while not Player1_input.isnumeric():
        Player1_input = input("Wrong format: please enter a single number with no spaces or commas ")
    Player1_input = int(Player1_input)
    Player2_input = input("How much do you think the " + objects[i].object + " costs, player two? " + objects[i].description + " Put your answer as an integer: ")
    while not Player2_input.isnumeric():
        Player2_input = input("Wrong format: please enter a single number with no spaces or commas: ")
    Player2_input = int(Player2_input)
    if abs(objects[i].cost - Player1_input) < abs(objects[i].cost - Player2_input):
        print("You win this round, player one!")
        Player1_score += 1
    elif abs(objects[i].cost - Player1_input) > abs(objects[i].cost - Player2_input):
        print("You win this round, player two!")
        Player2_score += 1
    else:
        print("It's a tie")
    print("The exact answer " " is $" + str(objects[i].cost) + " USD.")
    i = i + 1

if Player1_score < Player2_score:
    print("You win player two! Congratulations! You got " + str(Player2_score) + " points. Player one, you got " + str(
        Player1_score) + " points.")
elif Player2_score < Player1_score:
    print("You win player one! Congratulations! You got " + str(Player1_score) + " points. Player one, you got " + str(Player2_score) + " points")
elif Player1_score == Player2_score and 0 < Player2_score or 0 < Player1_score:
    print("It is an overall tie! Congratulations to both of you! Both of your scores are five!")




