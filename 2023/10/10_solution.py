def is_valid_pos(r: int, c: int) -> bool:
    if 0 <= r < maze_size[0] and 0 <= c < maze_size[1]:
        return True
    return False


def look_around(r: int, c: int) -> None:
    for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        i, j = r + direction[0], c + direction[1]
        is_valid = False

        if is_valid_pos(i, j) and maze[i][j] in valid_pipes and (i, j) not in moves_log:
            current_symbol, next_symbol = maze[r][c], maze[i][j]

            if r != i: # below or above
                if i > r and (current_symbol in ['|', 'F', '7', 'S'] and next_symbol in ['|', 'L', 'J']): 
                    is_valid = True # next symbol is below the current one |, L, J
                elif i < r and (current_symbol in ['|', 'L', 'J', 'S'] and next_symbol in ['|', 'F', '7']):
                    is_valid = True # next symbol is above the current one |, F, 7

            elif c != j: # left or right
                if j > c and (current_symbol in ['-', 'L', 'F', 'S'] and next_symbol in ['-', 'J', '7']):
                    is_valid = True # next symbol is to the right of the current one -, J, 7
                elif j < c and (current_symbol in ['-', 'J', '7', 'S'] and next_symbol in ['-', 'F', 'L']):
                    is_valid = True # next symbol is to the left of the current one -, L, F

        if is_valid:
            next_move_stack.append((i, j))
            moves_log.append((i, j))


with open('10_input.txt', "r") as f:
    data = f.readlines()

maze, moves_log, next_move_stack = [], [], []
valid_pipes = ['|', '-', 'L', 'J', '7', 'F', 'S']

for i in range(len(data)):
    current_list = []
    for j in range(len(data[i])):
        current_symbol = data[i][j]
        if current_symbol == '\n':
            continue
        current_list.append(current_symbol)
        if current_symbol == 'S':
            next_move_stack.append((i, j))
            moves_log.append((i, j))

    maze.append(current_list)        

maze_size = [len(maze), len(maze[0])]

while next_move_stack:
    r, c = next_move_stack.pop()
    look_around(r, c)

print(f'Part 1 Answer: {len(moves_log)//2}')
