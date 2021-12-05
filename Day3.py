def main():
    # haetaan data tiedostosta
    positions = []
    with open('./res/Day3.txt', 'r') as data:
        for line in data:
            positions.append(line.strip())

    part1(positions)
    part2(positions)
    

# Filtteröidään ne joissa haluttu bitti annetussa positiossa
def byte_filter(variable, pos, bit):
    if variable[pos] == bit:
        return True
    else:
        return False

# Selvitetään onko 1 vai 0 yleisempi positiossa

def most_common_bit(lines, pos):
    sum_1 = len(list(filter(lambda x: byte_filter(x, pos, '1'), lines)))
    if sum_1 >= len(lines)/2:
        return '1'
    else:
        return '0'

def lest_common_bit(lines, pos):
    sum_1 = len(list(filter(lambda x: byte_filter(x, pos, '1'), lines)))
    if sum_1 < len(lines)/2:
        return '1'
    else:
        return '0'

# part 1
def part1(positions):
    gamma = '0b'
    epsilon = '0b'

    for i, value in enumerate(positions[0]):
        bit = most_common_bit(positions, i)
        if bit == '1':
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print('Part1:')
    print(f'gamma: {gamma}, epsilon: {epsilon}')
    print(int(gamma, 2) * int(epsilon, 2))

def oxygen(positions, i):
    while len(positions) > 1:
        # Selvitetään position yleisin bitti
        bit = most_common_bit(positions, i)
        # Filtteröidään pois ne missä positiossa väärä bitti
        positions = list(filter(lambda x: byte_filter(x, i, bit), positions))
        return oxygen(positions, i+1)
    return positions

def CO2(positions, i):
    while len(positions) > 1:
        # Selvitetään position yleisin bitti
        bit = lest_common_bit(positions, i)
        # Filtteröidään pois ne missä positiossa väärä bitti
        positions = list(filter(lambda x: byte_filter(x, i, bit), positions))
        return CO2(positions, i+1)
    return positions

def part2(positions):
    o = oxygen(positions, 0)
    c = CO2(positions, 0)
    print('Part 2:')
    print(f'Oxygen: {o}')
    print(f'CO2: {c}')
    o = '0b' + o[0]
    c = '0b' + c[0]
    print(int(o, 2) * int(c, 2))

if __name__ == '__main__':
    main()