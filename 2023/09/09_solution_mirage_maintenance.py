from collections import deque

def check_all_elements_are_zero(some_list: list) -> bool:
    for item in some_list:
        if item != 0:
            return False
    return True


def extrapolate_next_value(some_list: list) -> None:
    list_length = len(some_list)
    levels.append(some_list)
    new_list = deque()

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
            preceeding_list.appendleft(preceeding_list[0] - (current_list[0]))
            preceeding_list.append(preceeding_list[-1] + current_list[-1])


with open('09_input.txt', "r") as f:
    data = f.readlines()

total_sum_pt_1 = 0
total_sum_pt_2 = 0

for row in data:
    levels = []
    starting_sequence = deque(int(x) for x in row.rstrip().split())

    extrapolate_next_value(starting_sequence)
    total_sum_pt_1 += levels[0][-1]
    total_sum_pt_2 += levels[0][0]

print(f'Part 1 Answer: {total_sum_pt_1}')
print(f'Part 2 Answer: {total_sum_pt_2}')
