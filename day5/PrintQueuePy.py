import sys

rules = []
page_orders = []
with open(sys.argv[1]) as f:
    content = f.read()
    parts = content.split('\n\n')
    rules = parts[0].splitlines()
    page_orders = parts[1].splitlines()


rules_matrix = {}
for rule in rules:
    parts = rule.split('|')
    if parts[0] not in rules_matrix:
        rules_matrix[parts[0]] = [parts[1]]
    elif parts[1] not in rules_matrix[parts[0]]:
        rules_matrix[parts[0]].append(parts[1])

sum = 0
pages_list = [line.split(',') for line in page_orders]
for order in pages_list:
    incorrect = 0
    for i in range(1, len(order)):
        if order[i] in rules_matrix.keys():
            for k in range(i-1, -1, -1):
                if order[k] in rules_matrix[order[i]]:
                    print(order[k], rules_matrix[order[i]])
                    incorrect += 1
    if incorrect == 0:
        sum += int(order[len(order)//2])
print(f"Sum of midpoint of matches: {sum}")
