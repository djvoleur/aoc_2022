#:Phe score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

# Opponent
# Rock=A,1 Paper=B,2 Scissors=C,3
# Me
# Rock=X,1 Paper=Y,2 Scissors=Z,3

# Win=6 Lose=3 Draw=0

def choice(choice):
    score=0

    if choice == "X":
        score += 1
    if choice == "Y":
        score += 2
    if choice == "Z":
        score += 3

    return score

def scoring(opponent, myself):
    score=0

    score += choice(myself)

    if (myself == "X" and opponent == "C") or (myself == "Y" and opponent == "A") or (myself == "Z" and opponent == "B"): # Win
        score += 6
    elif (myself == "X" and opponent == "A") or (myself == "Y" and opponent == "B") or (myself == "Z" and opponent == "C"): # Draw
        score += 3
    else: # Lose
        pass

    return score

def strategy(opponent, myself):
    score=0

    if myself == "Z": # Win
        score += 6
        if opponent == "A":
            score += choice("Y")
        elif opponent == "B":
            score += choice("Z")
        else:
            score += choice("X")
    elif myself == "Y": # Draw
        score += 3
        if opponent == "A":
            score += choice("X")
        elif opponent == "B":
            score += choice("Y")
        else:
            score += choice("Z")
    else: # Lose
        if opponent == "A":
            score += choice("Z")
        elif opponent == "B":
            score += choice("X")
        else:
            score += choice("Y")

    return score

def main():
    score=0
    score2=0

    input = open("day2_input")
    choices = input.readlines()

    for line in choices:
        hand=line.split()

        score += scoring(hand[0], hand[1])
        score2 += strategy(hand[0], hand[1])

    print(score)
    print(score2)

if __name__ == "__main__":
    main()
