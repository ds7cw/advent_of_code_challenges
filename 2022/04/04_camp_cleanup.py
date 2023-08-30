def check_for_overlap(h1: int, t1: int, h2: int, t2: int) -> int:
    head_comparison = total_overlap_dict[h1 <= h2]
    tail_comparison = total_overlap_dict[t1 >= t2]

    # If both the head and tail comparisons score 0.5, then their sum as an int is 1, otherwise 0 is returned
    return int(head_comparison + tail_comparison)


def check_for_partial_overlap(h1: int, t1: int, h2: int, t2: int) -> int:
    # The head and tail comparison variables can only ever hold a value of 1 or 0
    head_comparison = partial_overlap_dict[h1 <= h2 and h2 <= t1]
    tail_comparison = partial_overlap_dict[t1 >= t2 and t2 >= h1]

    return max(head_comparison, tail_comparison)


# Read the input and save to a variable for later use
with open("04_input.txt", "r") as f:
    data = f.readlines()

# For each pair where there is an overlap, we'll add 1 to the total_overlap_count
total_overlap_count = 0
# Using the below total_overlap_dict in the check_for_overlap method instead of an if/ else statement
total_overlap_dict = {True: 0.5, False: 0}

# The below variable will keep record of the partial overlaps
partial_overlap_count = 0
partial_overlap_dict = {True: 1, False: 0}

for row in data:
    elf1, elf2 = [[int(x) for x in pair.split("-")] for pair in row.split(",")]
    # First elf zone start value and second elf zone start value
    head1, head2 = elf1[0], elf2[0]
    # First elf zone end value and second elf zone end value
    tail1, tail2 = elf1[1], elf2[1]

    comparison1 = check_for_overlap(head1, tail1, head2, tail2)
    comparison2 = check_for_overlap(head2, tail2, head1, tail1)
    # Value of does_overlap will always be either 0 or 1
    does_overlap: int = max(comparison1, comparison2)

    total_overlap_count += does_overlap

    # We only check for a partial overlap in the event that there isn't a complete overlap
    if does_overlap == 0:
        comparison1_partial = check_for_partial_overlap(head1, tail1, head2, tail2)
        comparison2_partial = check_for_partial_overlap(head2, tail2, head1, tail1)

        partial_overlap_count += max(comparison1_partial, comparison2_partial)

print(f"Part 1 Answer: {total_overlap_count}")

print(f"Part 2 Answer: {partial_overlap_count + total_overlap_count}")
