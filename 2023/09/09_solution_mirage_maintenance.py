def check_all_elements_are_zero(some_list: list) -> bool:
    for item in some_list:
        if item != 0:
            return False
    return True


def extrapolate_next_value(some_list: list) -> None:
    list_length = len(some_list)
    levels.append(some_list)
    new_list = []

    for i in range(1, list_length):
        current_num = some_list[i] - some_list[i - 1]
        new_list.append(current_num)
    
    if not check_all_elements_are_zero(new_list):
        extrapolate_next_value(new_list)
    else:
        for j in range(len(levels) -1, -1, -1):
            if j == 0:
                return
            
            current_list, preceeding_list = levels[j], levels[j-1]
            preceeding_list.append(preceeding_list[-1] + current_list[-1])


with open('09_input.txt', "r") as f:
    data = f.readlines()

total_sum = 0

for row in data:
    levels = []
    starting_sequence = [int(x) for x in row.rstrip().split()]

    extrapolate_next_value(starting_sequence)
    total_sum += levels[0][-1]

print(f'Part 1 Answer: {total_sum}')
