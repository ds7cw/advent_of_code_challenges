def is_tail_close_enough(h, t, dirs) -> bool:
    if (t[0], t[1]) == (h[0], h[1]):
        return True

    for i, j in dirs.values():
        if (t[0], t[1]) == (i + h[0], j + h[1]):
            return True

    return False


# The below dict will be used to update the head position based on the "U", "R", "D", "L" character from the input
# The other key-value pairs will be used by the above function to cover the diagonals around the tail
directions = {
    "U": (-1, 0),
    "URC": (-1, 1),
    "R": (0, 1),
    "LRC": (1, 1),
    "D": (1, 0),
    "LLC": (1, -1),
    "L": (0, -1),
    "ULC": (-1, -1)
}

# Read the input and save to a variable for later use
with open("09_input.txt", "r") as f:
    data = f.readlines()

# Assume the head and the tail both start at the same position, overlapping
head = [0, 0]
tail = [0, 0]
h_last_known_pos = [0, 0]

# The below set will keep track of all positions the tail of the rope visits at least once, starting with (0, 0)
tail_visited_positions = set()
tail_visited_positions.add(tuple(tail))

# Iterate through ever row from the input data
for row in data:
    direction, steps = row.split()
    steps = int(steps)

    row_id, col_id = directions[direction]
    for _ in range(steps):
        h_last_known_pos[0], h_last_known_pos[1] = head[0], head[1]

        head[0] += row_id
        head[1] += col_id

        if is_tail_close_enough(head, tail, directions):
            # If the head is only one step away from the tail, regardless of direction, no action is required
            continue

        # If the head is further away than a single step, the tail assumes the head's position from the previous turn
        tail[0], tail[1] = h_last_known_pos[0], h_last_known_pos[1]
        # The tail's new position on the board is added to the set
        tail_visited_positions.add(tuple(tail))

print(f"Part 1 Answer: {len(tail_visited_positions)}")
