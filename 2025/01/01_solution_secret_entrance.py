with open("01_input.txt", "r") as f:
    data = f.readlines()

# Work in Progress
for row in data:
    r = row.strip()
    print(r)
    if r == 'R21':
        break
