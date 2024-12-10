import re

sum=0
state=1
with open('day3/input.txt') as f:
    for line in f:
        x = re.findall("mul\(\d+,\d+\)", line)
        for match in x:
            if match == "do()":
                state=1
            if match == "don't()":
                state=0
            if state == 1:
                numbers = re.findall(r'\d+', match)
                numbers = list(map(int, numbers))
                sum+=(numbers[0] * numbers[1])
print(f"Sum: {sum}")