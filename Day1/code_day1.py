with open("input.txt", mode="r", encoding="utf-8") as f:
    food_per_elf = [x.strip() for x in f]

calories = 0
calories_per_elf = []

# sum calories and make a list of calories per elf

for x in food_per_elf:
    if x != '':
        calories += int(x)

    elif x == '':
        calories_per_elf.append(calories)
        calories = 0

# print max value from sum of calories per elf to get answer
print(max(calories_per_elf))

# sort list descending and get sum of top 3, elves carrying the most calories

sorted_calories_per_elf = sum(sorted(calories_per_elf, reverse=True)[:3])

# print sum of top three elves carrying the most calories to get answer
print(sorted_calories_per_elf)



