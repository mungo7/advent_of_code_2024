
left = []
right = []

with open("day1_input.txt") as f:
    for line in f:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

left = sorted(left)
right = sorted(right)

diff = 0
print(left)
print(right)
for i in range(len(left)):
    diff += abs(right[i] - left[i])

print(diff)