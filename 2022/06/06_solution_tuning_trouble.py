def find_processed_characters(my_data: str, num: int) -> int:

    for idx in range(num, len(my_data)):
        current_group_list = my_data[idx - num: idx]
        current_group_set = {char for char in current_group_list}
        if len(current_group_set) == num:
            return idx


# Read the input and save to a variable for later use
with open("06_input.txt", "r") as f:
    data = f.readline()

# A start-of-packet marker consists of 4 distinct characters
packet_distinct_chars = 4
# A start-of-message marker consists of 14 distinct characters
message_distinct_chars = 14

print(f"Part 1 Answer: {find_processed_characters(data, packet_distinct_chars)}")
print(f"Part 1 Answer: {find_processed_characters(data, message_distinct_chars)}")
