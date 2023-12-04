with open("04_input.txt", "r") as f:
    data = f.readlines()

total = 0

for row in data:
    game_id, decks = row.rstrip().split(':')
    deck_1, deck_2 = decks.split('|')

    d_1_set = set(x for x in deck_1.split())
    d_2_set = set(x for x in deck_2.split())

    matching_nums = d_1_set.intersection(d_2_set)
    matching_nums_count = len(matching_nums)

    if matching_nums_count == 1:
        total += 1
    elif matching_nums_count > 1:
        total += 2**(matching_nums_count-1)

print(f'Part 1 Answer: {total}')
