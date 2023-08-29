def find_common_item(first: str, second: str) -> str:
    for char in first:
        if char in second:
            return char


def find_common_badge(row_one: str, row_two: str, row_three: str):
    for char in row_one:
        if char in row_two:
            if char in row_three:
                return char


# Read the input and save to a variable for later use
with open("03_input.txt", "r") as f:
    data = f.readlines()

# Lowercase item types a through z have priorities 1 through 26.
lower_dict = {chr(97 + i - 1): i for i in range(1, 27)}

# Uppercase item types A through Z have priorities 27 through 52.
upper_dict = {chr(65 + i - 1): (i + 26) for i in range(1, 27)}

# Combining the above dictionaries to use a single dict for both lowercase and uppercase keys
combined_dict = {**lower_dict, **upper_dict}

# This variable will hold the answer to part 1
total_sum = 0

# The list below will be holding 3 rows at a time
group_of_three = []

# This variable will hold the answer to part 2
badge_total_sum = 0

for row in data:

    # Find out the middle of the row and create variables holding each half using slicing
    mid_idx = len(row) // 2
    first_half, second_half = row[:mid_idx], row[mid_idx:]

    # Function takes the two halves as arguments, finds a common character and returns it
    common_item = find_common_item(first_half, second_half)

    # The int value sitting behind the common_type key is added to the total_sum
    total_sum += combined_dict[common_item]

    group_of_three.append(row)
    if len(group_of_three) == 3:
        # Once the size of the list reaches 3, call the find_common_badge function and unpack the list
        common_badge = find_common_badge(*group_of_three)
        # The int value sitting behind the common_badge key is added to the badge_total_sum
        badge_total_sum += combined_dict[common_badge]

        # Clear the list in anticipation of the next 3 rows
        group_of_three.clear()

print(f"Part 1 Answer: {total_sum}")
print(f"Part 2 Answer: {badge_total_sum}")
