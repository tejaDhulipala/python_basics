class Dog:

    def __init__(self, name, breed, gender, favorite_food, age, is_social):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.favorite_food = favorite_food
        self.age = age
        self.is_social = is_social
Dogs = [Dog("Teddy","Golden retriver","male","Turkey",6,False),
       Dog("Pepsi","Labrador","female","penut butter",6,False),
       Dog("Bethany","Chihuahua","female","Roast beef",2,True),
       Dog("Bear","German Shepard","female","Beef",4,False)
]
i=0
while i<len(Dogs):
    print(Dogs[i].name+" the "+Dogs[i].breed+" is a "+Dogs[i].gender+" who's favorite food is "+Dogs[i].favorite_food+", and is " + str(Dogs[i].age)+" years old. It is " + str(Dogs[i].is_social) + " that this dog is social.")
    i=i+1
Choice=input("Which dog do you think you want the most? Put in the name of that dog: ")
print(Choice)

if Choice == "Teddy" or Choice == "teddy":
    Choice2 = int(input("How much do you think this dog costs? Put your guess(as an integer) here: "))
    if 1300 < Choice2 < 1700:
        print("You have won the guessing game! You now get this Dog 10% off!")
    else:
        print("That is the wrong answer!")
elif Choice == "Pepsi" or Choice == "pepsi":
    Choice3 = int(input("How much do you think this dog costs? Put your guess(as an integer) here: "))
    if 250 < Choice3 < 650:
        print("You have won the guessing game! You now get this Dog 10% off!")
    else:
        print("That is the wrong answer!")
elif Choice.lower() == "bethany":
    Choice4 = int(input("How much do you think this dog costs? Put your guess(as an integer) here: "))
    if 300 < Choice4 < 700:
        print("You have won the guessing game! You now get this Dog 10% off!")
    else:
        print("That is the wrong answer!")
elif Choice == "Bear" or Choice == "bear":
    Choice5 = int(input("How much do you think this dog costs? Put your guess(as an integer) here: "))
    if 400 < Choice5 < 800:
        print("You have won the guessing game! You now get this Dog 10% off!")
    else:
        print("That is the wrong answer!")
else:
    print("It really isn't that hard to type the name of a dog.")