def check_visibility(idxi: int, idxj: int):
    current_tree = matrix[i][j]

    left = [i, 0]
    while left[1] < idxj:
        if matrix[left[0]][left[1]] >= current_tree:
            break
        left[1] += 1
    else:
        return True

    right = [i, len(matrix[i]) - 1]
    while right[1] > idxj:
        if matrix[right[0]][right[1]] >= current_tree:
            break
        right[1] -= 1
    else:
        return True

    up = [0, j]
    while up[0] < idxi:
        if matrix[up[0]][up[1]] >= current_tree:
            break
        up[0] += 1
    else:
        return True

    down = [(len(matrix) - 1), j]
    while down[0] > idxi:
        if matrix[down[0]][down[1]] >= current_tree:
            return False
        down[0] -= 1

    return True


# Read the input and save to a variable for later use
with open("08_input.txt", "r") as f:
    data = f.readlines()

matrix = [[int(el) for el in sub_list.rstrip()] for sub_list in data]

rows_count = len(matrix)
cols_count = len(matrix[0])

visible_trees = 2 * rows_count + (2 * cols_count) - 4
visibility_score = {True: 1, False: 0}


for i in range(1, rows_count - 1):
    for j in range(1, cols_count - 1):
        result = check_visibility(i, j)
        visible_trees += visibility_score[result]

print(f"Part 1 Answer: {visible_trees}")
