choice_scoring = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

encryption = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors",

    "X" : "loss",
    "Y" : "draw",
    "Z" : "win",
}

result_scoring = {
    "win": 6,
    "draw": 3,
    "loss": 0
}

def calculate_result(their_choice, required_result):
    score = 0
    their_choice = encryption[their_choice]
    required_result = encryption[required_result]
    if required_result == "draw":
        your_choice = their_choice

    elif required_result == "loss":
        if their_choice == "scissors":
            your_choice = "paper"
        elif their_choice == "rock":
            your_choice = "scissors"
        elif their_choice == "paper":
            your_choice = "rock"

    elif required_result == "win":
        if their_choice == "scissors":
            your_choice = "rock"
        elif their_choice == "rock":
            your_choice = "paper"
        elif their_choice == "paper":
            your_choice = "scissors"

    score += result_scoring[required_result]
    score += choice_scoring[your_choice]

    return score

with open ("Day2\input.txt", "r") as input:
    data = (input.read()).split("\n")

score = 0

for row in data:
    their_choice, required_result = row.split(" ")
    score += calculate_result(their_choice, required_result)

print(f"Your total Score is {score}")