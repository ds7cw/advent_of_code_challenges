# Part 1
def margin_of_error(list_collection: list) -> int:
    result = list_collection[0]
    for item in list_collection[1:]:
        result *= item
    
    return result


with open('06_input.txt', "r") as f:
    data = f.readlines()

time_list = [int(x) for x in data[0].split(':')[1].strip().split()]
distance_list = [int(x) for x in data[1].split(':')[1].strip().split()]

counter = 0
stats = {i: 0 for i in range(1, len(time_list) + 1)}

for seconds, distance in zip(time_list, distance_list):
    counter +=1 

    for i in range(1, seconds):
        result = i * (seconds - i)
        if result > distance:
            stats[counter]+= 1

print(f'Part 1 Answer: {margin_of_error([val for val in stats.values()])}')


# Part 2
time = int(''.join([x for x in data[0].split(':')[1].strip().split()]))
distance = int(''.join([x for x in data[1].split(':')[1].strip().split()]))

first = 0
last = 0

for i in range(1, time):
    if i * (time - i) > distance:
        first = i
        break

for j in range(time, 0, -1):
    if j * (time - j) > distance:
        last = j
        break

print(f'Part 2 Answer: {last - first + 1}')
