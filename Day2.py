import pyperclip

def part1():
    data = []
    with open('./res/Day2.txt', 'r') as f:
        for line in f:
            data.append(line.split())
    
    forward = 0
    depth = 0

    for step in data:
        if step[0] == 'forward':
            forward += int(step[1])
        elif step[0] == 'down':
            depth += int(step[1])
        else:
            depth -= int(step[1])

    print('Part1: {result}'.format(result=(forward*depth)))
    # pyperclip.copy(str(forward*depth))

def part2():
    data = []
    with open('./res/Day2.txt', 'r') as f:
            for line in f:
                data.append(line.split())
        
    forward = 0
    depth = 0
    aim = 0

    for step in data:
        if step[0] == 'forward':
            forward += int(step[1])
            depth += int(step[1]) * aim
        elif step[0] == 'down':
            aim += int(step[1])
        else:
            aim -= int(step[1])
    
    print('Part2: {result}'.format(result = (forward*depth)))
    # pyperclip.copy(str(forward*depth))

if __name__ == '__main__':
    part1()
    part2()