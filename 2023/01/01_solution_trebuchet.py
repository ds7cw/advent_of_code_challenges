def solution_part_two(rows):
    total = 0

    for row in rows:
        word_order = {}

        for key in nums.keys():
            if key in row:
                current_string = row
                counter = 0
                while key in current_string:
                    idx = current_string.index(key) + counter
                    word_order[idx] = key
                    current_string = current_string[1:]
                    counter += 1

        ordered_word_order = sorted(word_order.items(), key=lambda x: x[0])
        digits = []
        
        for idx, char in enumerate(row, start=0):
            if char.isdigit():
                digits.append(char)
            elif ordered_word_order: 
                if idx == ordered_word_order[0][0]:
                    digits.append(nums[ordered_word_order[0][1]])
                elif len(ordered_word_order) > 1 and idx == ordered_word_order[-1][0]:
                    digits.append(nums[ordered_word_order[-1][1]])
        
        total += int(f'{digits[0]}{digits[-1]}')
    return total


with open("01_input.txt", "r") as f:
    data = f.readlines()

nums = {'one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

print(f'Part 2 Answer: {solution_part_two(data)}')