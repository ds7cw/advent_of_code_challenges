def check_visibility(idxi: int, idxj: int) -> bool:
    current_tree = matrix[i][j]
    max_row_idx = len(matrix) - 1
    max_col_idx = len(matrix[0]) - 1
    is_visible = False

    # Use the below variables to keep track of the tree cover available in each direction (Part 2)
    trees_left, trees_right, trees_up, trees_down = (0, 0, 0, 0)

    left = [i, idxj - 1]
    # Start from the tree closest to the current tree's left side
    # Iterate through trees until you either reach a tree which is equally tall or taller, or until you reach the edge
    while left[1] >= 0:
        # Add one more tree to the tree cover in that direction at the start of each iteration
        trees_left += 1
        if matrix[left[0]][left[1]] >= current_tree:
            break
        left[1] -= 1
    else:
        # Reaching the end of the while loop without breaking means the tree is visible
        is_visible = True

    right = [i, idxj + 1]
    while right[1] <= max_col_idx:
        trees_right += 1
        if matrix[right[0]][right[1]] >= current_tree:
            break
        right[1] += 1
    else:
        is_visible = True

    up = [idxi - 1, j]
    while up[0] >= 0:
        trees_up += 1
        if matrix[up[0]][up[1]] >= current_tree:
            break
        up[0] -= 1
    else:
        is_visible = True

    down = [idxi + 1, j]
    while down[0] <= max_row_idx:
        trees_down += 1
        if matrix[down[0]][down[1]] >= current_tree:
            break
        down[0] += 1
    else:
        is_visible = True

    # Compare the current tree scenic score to the current highest score and update the score
    highest_scenic_score[0] = (max(highest_scenic_score[0], (trees_left * trees_right * trees_up * trees_down)))

    return is_visible


# Read the input and save to a variable for later use
with open("08_input.txt", "r") as f:
    data = f.readlines()

# Every row as a sub-list containing integer values
matrix = [[int(el) for el in sub_list.rstrip()] for sub_list in data]

rows_count = len(matrix)
cols_count = len(matrix[0])

# Count all visible trees along the perimeter/ edge
visible_trees = 2 * rows_count + (2 * cols_count) - 4
visibility_score = {True: 1, False: 0}
# Start with a highest scenic score of 0 (Part 2 challenge)
highest_scenic_score = [0]

# Iterate through every column on every row, except the ones on the perimeter/ edge
for i in range(1, rows_count - 1):
    for j in range(1, cols_count - 1):
        # If the check_visibility returns True, add 1 to the visible_trees value
        result = check_visibility(i, j)
        visible_trees += visibility_score[result]

print(f"Part 1 Answer: {visible_trees}")
print(f"Part 2 Answer: {highest_scenic_score[0]}")
