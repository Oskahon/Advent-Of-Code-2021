import re

def get_lines(file_location):
    with open(file_location, 'r') as file:
        data = file.read().split('\n')
    return data

def get_coordinates(data):
    coordinates = []
    for line in data:
        coordinates.append([(int(x), int(y)) for (x, y) in re.findall(r'(\d+),(\d+)', line)])
    return coordinates

def get_width(coordinates):
    max_coord = 0
    for line in coordinates:
        for coordinate in line:
            if max(coordinate) > max_coord:
                max_coord = max(coordinate)
    return max_coord

def create_grid(width):
    grid = [None] * (width + 1)
    for i in range(len(grid)):
        grid[i] = [0] * (width + 1)
    return grid

def mark_lines(coordinates, grid):
    count = 1
    for line in coordinates:
        # uncomment for part 1
        # if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            change_x = line[1][0] - line[0][0]
            change_y = line[1][1] - line[0][1]
            if not change_x == 0 and not change_y == 0:
                if change_x > 0 and change_y > 0:
                    for i in range(change_x+1):
                        grid[line[0][1]+i][line[0][0]+i] += 1
                elif change_x < 0 and change_y < 0:
                    for i in range(abs(change_x)+1):
                        grid[line[0][1]-i][line[0][0]-i] += 1
                elif change_x > 0 and change_y < 0:
                    for i in range(abs(change_x)+1):
                        grid[line[0][1]-i][line[0][0]+i] += 1
                elif change_x < 0 and change_y > 0:
                    for i in range(abs(change_x)+1):
                        grid[line[0][1]+i][line[0][0]-i] += 1
            elif not change_x == 0:
                if change_x > 0:
                    for i in range(change_x+1):
                        grid[line[0][1]][line[0][0]+i] += 1
                elif change_x < 0:
                    for i in range(abs(change_x)+1):
                        grid[line[0][1]][line[0][0]-i] += 1
            elif not change_y == 0:
                if change_y > 0:
                    for i in range(change_y+1):
                        grid[line[0][1]+i][line[0][0]] += 1
                elif change_y < 0:
                    for i in range(abs(change_y)+1):
                        grid[line[0][1]-i][line[0][0]] += 1

    return grid

def part1_2():
    coordinates = get_coordinates(get_lines('./res/Day5.txt'))
    grid = create_grid(get_width(coordinates))
    mark_lines(coordinates, grid)
    overlap = 0
    for line in grid:
        # print(line)
        overlap += sum(i > 1 for i in line) 
    print(overlap)

def main():
    part1_2()

if __name__ == '__main__':
    main()