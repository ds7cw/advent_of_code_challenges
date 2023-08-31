def cleanup_matrix(stacks_list: list) -> list:
    # '[F] [W] [B] [L] [P] [D] [L] [N] [G]\n' length is 36
    row_length = len(stacks_list[7])
    # Start at index 1 for each row and increase by 4 on the next iteration to jump over to the next letter
    IDX_STEP = 4
    result = []

    for row in stacks_list:
        temp_list = [row[idx] for idx in range(1, row_length, IDX_STEP)]
        result.append(temp_list)

    return result


def rotate_matrix(stacks_list: list) -> list:
    rows_number = len(stacks_list)
    columns_number = len(stacks_list[0])
    result = [[] for _ in range(columns_number)]

    for i in range(columns_number):
        for j in range(rows_number - 1, -1, -1):
            if stacks_list[j][i].isalpha():
                result[i].append(stacks_list[j][i])

    return result


def final_message(some_list: list) -> str:
    return ''.join([column[-1] for column in some_list])


# Read the input and save to a variable for later use
with open("05_input.txt", "r") as f:
    data = f.readlines()

# We grab only the stacks data to build our matrix
stacks_matrix = data[:8]

# The below function cleans up the matrix by removing the [ ] and unnecessary white spaces
stacks_matrix = cleanup_matrix(stacks_matrix)

# The below function turns each column into a row
stacks_matrix = rotate_matrix(stacks_matrix)

# Make a copy of the matrix to be used to solve the second part of the challenge iterating only once through the data
matrix_part_two_copy = [sublist[:] for sublist in stacks_matrix]

# data[9] is an empty line, commands start from data[10]
for row in data[10:]:
    # The list comprehension extracts [2, 2, 8] from the 'move 2 from 2 to 8' row
    quantity, start_pos, end_pos = [int(num) for num in row.split() if not num.isalpha()]
    for _ in range(quantity):
        # Pop the start position column and assign it to the destination stack
        current = stacks_matrix[start_pos - 1].pop()
        stacks_matrix[end_pos - 1].append(current)

    # Moving multiple elements from one stack to another in one go
    matrix_part_two_copy[end_pos - 1].extend(matrix_part_two_copy[start_pos - 1][-quantity:])
    matrix_part_two_copy[start_pos - 1] = matrix_part_two_copy[start_pos - 1][: -quantity]

print(f"Part 1 Answer: {final_message(stacks_matrix)}")
print(f"Part 2 Answer: {final_message(matrix_part_two_copy)}")
