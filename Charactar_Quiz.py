class gods:
    def __init__(self, name, characteristic):
        self.name = name
        self.chars = characteristic

    def similar(self, answers):
        assert type(answers) == list
        return len(set(answers + self.chars)) <= len(self.chars) + 1
end_outcomes = [
    [[["Hephaestus"], ["Hephaestus"], ["Hephaestus"], ["Hephaestus"]], [["Hades"], ["Hephaestus"], ["Hephaestus"], ["Hephaestus"]], [["Hephaestus"], ["Hephaestus"], ["Hephaestus"], ["Hephaestus"]], [["Hades"], ["Hephaestus"], ["Hephaestus"], ["Hephaestus"]]],
    [[["Ares"], ["Poseidon"], ["Pyriphlegethon"], ["Pyriphlegethon"]], [["Poseidon"], ["Poseidon"], ["Poseidon"], ["Poseidon"]], [["Poseidon"], ["Poseidon"], ["Athena"], ["Poseidon"]], [["Styx"],["Poseidon"],["Poseidon"],["Styx"]]],
    [[["Ares"], ["Hestia"], ["Hestia"], ["Ares"]], [["One of the Potamoi"], ["One of the Potamoi"], ["Athena"], ["Hephaestus"]], [["Zeus"], ["Zeus"], ["Athena"], ["Athena"]], [["Hades"], ["Hephaestus"], ["Hades"], ["Hephaestus"]]],
    [[["Zeus"], ["Zeus"], ["Zeus"], ["Ares"]], [["Zeus"], ["Eos"], ["Athena"], ["lol i dont know):"]], [["Zues"], ["Zues"], ["Athena"], ["Athena"]], [["Hades"], ["Zeus"], ["Hades"], ["Hades"]]]
]
Q1 = input("What is your favorite color? Type in the letter of your favorite choice.\na: Red\nb: Blue\nc: "
               "White\nd: black\n ").strip().lower()
while Q1 not in "abcd":
    Q1 = input("You dun goofed up! Try again: ").strip().lower()
color = ord(Q1) - ord('a')
Q2 = input("What is your favorite element? Type in the letter of your favorite choice.\na: Fire\nb: Water\nc: "
               "earth\nd: air\n ").strip().lower()
element = ord(Q2) - ord("a")
Q3 = input("What is your best quality? Type in the letter of your favorite choice.\na: Strength\nb: Kindness\nc: "
               "Wise\nd:Hard-Working\n ").strip().lower()

quality = ord(Q3) - ord("a")
print("You are " + str(end_outcomes[element][color][quality])+"!")
