def is_safe_report(levels):
    direction = 0
    for i in range(len(levels) - 1):
        if levels[i] < levels[i + 1]:
            if direction == -1:
                return False
            direction = 1
        elif levels[i] > levels[i + 1]:
            if direction == 1:
                return False
            direction = -1
        else:
            return False
        
        spacing = abs(levels[i] - levels[i + 1])
        if spacing < 1 or spacing > 3:
            return False
    return True

safe = 0

with open('input.txt') as f:
    for report in f:
        levels = list(map(int, report.split()))
        if is_safe_report(levels):
            safe += 1

print(safe)
