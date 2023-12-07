def is_valid_cell(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return True
    return False

def has_symbol_as_neighbour(row, col):
    
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
        'upper_left_corner': (-1, -1),
        'upper_right_corner': (-1, 1),
        'lower_left_corner': (1, -1),
        'lower_right_corner': (1, 1),
    }

    for direction in directions.values():
        row_dir, col_dir = direction
        neighbour_row, neighbour_col = int(row) + row_dir, int(col) + col_dir
        if is_valid_cell(neighbour_row, neighbour_col):
        
            if matrix[neighbour_row][neighbour_col] != '.' and not matrix[neighbour_row][neighbour_col].isdigit():
                return True
    return False


with open("03_input.txt", "r") as f:
    data = f.readlines()

matrix = [[char for char in row.rstrip()] for row in data]
total = []

for i in range(len(matrix)):
    
    coordinates = []
    current_num = ''

    for j in range(len(matrix[i])):

        if matrix[i][j].isdigit():
            current_num += matrix[i][j]
            coordinates.append((i, j))

        if j == len(matrix[i]) - 1 or not matrix[i][j].isdigit():
            while coordinates:
                r,c = coordinates.pop()
            
                if has_symbol_as_neighbour(r, c):
                    total.append(int(current_num))
                    coordinates.clear()
                    break
                
            current_num = ''

print(f'Part 1 Answer: {sum(total)}')
