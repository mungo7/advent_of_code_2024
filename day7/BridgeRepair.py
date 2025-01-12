
with open('input.txt') as f:
    for line in f:
        line = line.split(':')
        test_val = line[0]
        num_ops = []
        for numeric_operator in line[1]:
            num_ops.append(numeric_operator)
        print(test_val, num_ops)
        