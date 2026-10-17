number_file = []

with open("p2.txt") as file:
    for line in file:
        number_file.append(int(line))

number_file.sort(reverse=True)

duplicates = len(number_file) - len(set(number_file))

print("Found", duplicates, "duplicates")
