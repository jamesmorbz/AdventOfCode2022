choice_scoring = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

encryption = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors",

    "X" : "rock",
    "Y" : "paper",
    "Z" : "scissors",
}

result_scoring = {
    "win": 6,
    "draw": 3,
    "loss": 0
}

def calculate_result(their_choice, your_choice):
    score = 0
    their_choice = encryption[their_choice]
    your_choice = encryption[your_choice]
    if your_choice == their_choice:
        result = "draw"
    elif your_choice == "rock":
        if their_choice == "scissors":
            result = "win"
        elif their_choice == "paper":
            result = "loss"
    elif your_choice == "scissors":
        if their_choice == "rock":
            result = "loss"
        elif their_choice == "paper":
            result = "win"
    elif your_choice == "paper":
        if their_choice == "rock":
            result = "win"
        elif their_choice == "scissors":
            result = "loss"

    score += result_scoring[result]
    score += choice_scoring[your_choice]

    return score

with open ("Day2\input.txt", "r") as input:
    data = (input.read()).split("\n")

score = 0

for row in data:
    their_choice, your_choice = row.split(" ")
    score += calculate_result(their_choice, your_choice)

print(f"Your total Score is {score}")