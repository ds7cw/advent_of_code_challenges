def process_data(range_collection: list, some_collection: list):

    for i in range(len(some_collection)):

        for item in range_collection:
            seed = some_collection[i]
            first, second, amount = item

            if second <= seed < (second + amount):
                some_collection[i] = (seed - second) + first
                break

    return some_collection


with open('05_input.txt', "r") as f:
    data = f.readlines()

seeds_collection = [int(x) for x in data[0].split(': ')[1].strip().split()]
temporary = []

for row in data[2:]:
    row_first_char = row[0]

    if row_first_char.isspace():
        seeds_collection = process_data(temporary, seeds_collection)

    elif row_first_char.isdigit():
         temporary.append([int(x) for x in row.rstrip().split()])

    elif row_first_char.isalpha():
        temporary.clear()
else:
    seeds_collection = process_data(temporary, seeds_collection)

print(f'Part 1 Answer: {min(seeds_collection)}')
