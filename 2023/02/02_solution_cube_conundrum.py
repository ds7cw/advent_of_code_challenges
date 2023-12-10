with open("02_input.txt", "r") as f:
    data = f.readlines()

allowed_cubes = {'red': 12, 'green': 13, 'blue': 14}
powers_list = []

for row in data:
    game_data, cubes = row.split(': ')
    game_id = int(game_data.split()[1])
 
    sets = cubes.rstrip().split('; ')
    temp_dict = {'red': 0, 'green': 0, 'blue': 0}

    for cubes_set in sets:
        for pair in cubes_set.split(', '):
            cubes_count, colour = pair.split()
            temp_dict[colour]= max(temp_dict[colour], int(cubes_count))
 
    powers_list.append(temp_dict['red'] * temp_dict['green'] * temp_dict['blue'])

print(f'Part 2 Answer: {sum(powers_list)}')


# Part 1
possible_games = []

for row in data:
    game_data, cubes = row.split(': ')
    game_id = int(game_data.split()[1])
 
    cubes.rstrip()
    sets = cubes.split('; ')
    flag_possible = True

    for cubes_set in sets:
        for pair in cubes_set.split(', '):
            cubes_count, colour = pair.split()
            cubes_count = int(cubes_count)

            if cubes_count > allowed_cubes[colour]:
                flag_possible = False
                break
        if not flag_possible:
            break
    
    else:
        possible_games.append(game_id)

print(f'Part 1 Answer: {sum(possible_games)}')
