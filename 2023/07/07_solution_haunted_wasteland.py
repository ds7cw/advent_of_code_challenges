with open('07_input.txt', "r") as f:
    data = f.readlines()

directions = [x for x in data[0].rstrip()]
dir_idx = 0
dir_len = len(directions)
steps = 0

maps = {row[0:3]: row[7:15].split(', ') for row in data[2:]}
left_right = {'L': 0, 'R': 1}

current_map = maps['AAA']


while True:
    if dir_idx == dir_len:
        dir_idx = 0

    my_dir = directions[dir_idx]

    next_step = current_map[left_right[my_dir]]
    steps += 1

    if next_step == 'ZZZ':
        break

    dir_idx += 1
    current_map = maps[next_step]

print(f'Part 1 Answer: {steps}')
