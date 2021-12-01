from os import read


def main():
    readings = []
    with open('./res/Day1.txt', 'r') as data:
        for reading in data:
            readings.append(int(reading))
    
    # Part 1
    depth_increase = 0

    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            depth_increase += 1
    
    print('part 1: {sum}'.format(sum = depth_increase))
    
    # Part 2
    depth_increase = 0

    for i in range(len(readings)):
        if i < len(readings)-3:
            sum1 = 0
            sum2 = 0
            for x in range(i, i+3):
                sum1 += readings[x]
            for y in range(i+1, i+4):
                sum2 += readings[y]

            if sum2 > sum1:
                depth_increase += 1
    
    print('part 2: {sum}'.format(sum = depth_increase))

if __name__ == '__main__':
    main()