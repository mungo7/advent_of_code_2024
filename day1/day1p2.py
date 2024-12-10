
left = {}
right = []
with open('day1_input.txt') as f:
    for line in f:
        l = int(line.split()[0])
        r = int(line.split()[1])
        if l in left:
            continue
        else:
            left[l] = 0
        right.append(r)

for id in right:
    if id in left:
        left[id] += 1

sum = 0
for key in left.keys():
    sum += key*left[key]

print(sum)


