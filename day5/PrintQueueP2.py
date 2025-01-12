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
corrected_sum = 0
pages_list = [line.split(',') for line in page_orders]

def identify_correct(order):
    for i in range(1, len(order)):
        if order[i] in rules_matrix.keys():
            for k in range(i-1, -1, -1):
                if order[k] in rules_matrix[order[i]]:
                    return False
    return True

def get_midpoint(order):
    return int(order[len(order)//2])

def sort_order(order):
    print("Running sort")
    while not identify_correct(order):
        for i in range(1, len(order)):
            if order[i] in rules_matrix.keys():
                for k in range(i-1, -1, -1):
                    if order[k] in rules_matrix[order[i]]:
                        order[i], order[k] = order[k], order[i]
                        break
    return order
        
for order in pages_list:
    res = identify_correct(order)
    if res:
        sum += get_midpoint(order)
    else:
        res = sort_order(order)
        corrected_sum += get_midpoint(res)

print(f"Sum of midpoint of matches: {sum}")
print(f"Sum of midpoint of corrected matches: {corrected_sum}")
