#   Solution to Part 1
def win(p2_hand):

    return pts_per_choice[p2_hand] + pts_win_loss_draw["win"]


def loss(p2_hand):

    return pts_per_choice[p2_hand] + pts_win_loss_draw["loss"]


p2_overall_score = 0

# How many points do we get for a win, loss and a draw
pts_win_loss_draw = {
    "win": 6,
    "loss": 0,
    "draw": 3
}

# How many points correspond to the player's chosen shape
pts_per_choice = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

# The key is player 1's chosen shape. The value is the shape player 2 needs in order to beat p1's shape
winning_shape = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

win_or_loss = {True: "win", False: "loss"}

# Read the input and save to a variable for later use
with open("02_input", "r") as f:
    data = f.readlines()

# Iterate through every round
for item in data:

    # Read and assign the chosen shapes for player 1 and player 2
    p1_choice, p2_choice = item.split()

    # Find the points corresponding to each player's chosen shape and do the subtraction
    p1_minus_p2 = pts_per_choice[p1_choice] - pts_per_choice[p2_choice]

    # If the result is zero, they both used the same shape and the outcome of the game is a draw
    if p1_minus_p2 == 0:
        # Draw
        p2_overall_score += pts_per_choice[p2_choice] + pts_win_loss_draw["draw"]
        continue

    # The shape needed to beat player 1
    needed_to_win = winning_shape[p1_choice]

    # Does player 2 have the shape required to beat player 1
    is_winning_hand = needed_to_win == p2_choice

    # If he has the shape then the win() function is called, otherwise the loss() function is called
    # Add the result to the player's overall score
    p2_overall_score += locals()[win_or_loss[is_winning_hand]](p2_choice)

print(f"Part 1 Answer: {p2_overall_score}")

#   ----------------------------------------------------------------

#   Solution to Part 2, reusing code from Part 1


def win(p1_hand):
    p2_hand = winning_shape[p1_hand]
    return pts_per_choice[p2_hand] + pts_win_loss_draw["win"]


def loss(p1_hand):
    p2_hand = losing_shape[p1_hand]
    return pts_per_choice[p2_hand] + pts_win_loss_draw["loss"]


def draw(p1_hand):
    return pts_per_choice[p1_hand] + pts_win_loss_draw["draw"]


p2_overall_score = 0

# How many points do we get for a win, loss and a draw
pts_win_loss_draw = {
    "win": 6,
    "loss": 0,
    "draw": 3
}

# How many points correspond to the player's chosen shape
pts_per_choice = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

# The key is player 1's chosen shape. The value is the shape player 2 needs in order to beat p1's shape
winning_shape = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

# The key is player 1's chosen shape. The value is the shape player 2 needs in order to lose the round
losing_shape = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

win_loss_draw = {"Z": "win", "X": "loss", "Y": "draw"}

# Read the input and save to a variable for later use
with open("02_input", "r") as f:
    data = f.readlines()

# Iterate through every round
for item in data:

    # Read and assign the chosen shapes for player 1 and the expected outcome for the current round
    p1_choice, game_outcome = item.split()
    # Re-assign the game_outcome variable using the win_loss_draw dict
    game_outcome = win_loss_draw[game_outcome]

    # Call function "win", "loss" or "draw" depending on the game_output value
    # The function returns the score for the round and adds it to the overall score
    p2_overall_score += locals()[game_outcome](p1_choice)

print(f"Part 2 Answer: {p2_overall_score}")
