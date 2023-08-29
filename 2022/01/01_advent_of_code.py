# Part 1
# Read the input from a .txt file and save to a variable for later use
with open("01_input.txt", "r") as f:
    data = f.readlines()

# Dict "elves" will contain the elf# as a key, and the total calories carried as a value
elves = {}
# Calories sum to be reset to an empty list after the total calories for an elf have been calculated
current_sum = []
# Starting at #1
elf = 1
# max_elf stores the elf #number at index 0 and the total amount of calories at index 1
max_elf = [float("-inf"), 0]

for i in range(len(data)):
    if data[i] == "\n":

        # In case the last line is a \n
        if i == len(data) - 1:
            break

        elves[elf] = sum(current_sum)

        # If the current elf carries more calories than the max elf, the new max_elf is the current elf
        max_elf = [elf, elves[elf]] if elves[elf] > max_elf[1] else max_elf
        # Reset the sum and increment the elf #number in anticipation of the next elf
        current_sum = []
        elf += 1
        continue

    # Keep appending calories to the current sum until you reach a \n
    current_sum.append(int(data[i].strip("\n")))

# print(max_elf)
# Print the value behind elf #number ? from the elves dictionary
print(f"Part 1 Answer: {elves[max_elf[0]]}")

# Part 2
# Use list slicing on a sorted dict to grab the top 3 results in descending order
top_three = sorted(elves.items(), key=lambda x: -x[1])[:3]
# Calculate the sum of the calories for the top three elves
print(f"Part 2 Answer: {sum([item[1] for item in top_three])}")
