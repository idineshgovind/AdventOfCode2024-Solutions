# Combine Part 1 and Part 2
def main():
    with open("input.txt", "r") as file:
        grid = [line.strip() for line in file]
    total_part1 = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == 'X':
                for i in range(-1 if y > 2 else 0, 2 if y < len(grid) - 3 else 1):
                    for j in range(-1 if x > 2 else 0, 2 if x < len(grid) - 3 else 1):
                        if grid[y + i][x + j] == 'M' and grid[y + 2 * i][x + 2 * j] == 'A' and grid[y + 3 * i][x + 3 * j] == 'S':
                            total_part1 += 1
    print("part 1", total_part1)
    total_part2 = sum(
        1 for y in range(1, len(grid) - 1)
        for x in range(1, len(grid) - 1)
        if grid[y][x] == 'A'
        and {grid[y - 1][x - 1], grid[y + 1][x + 1]} == {'M', 'S'}
        and {grid[y + 1][x - 1], grid[y - 1][x + 1]} == {'M', 'S'}
    )
    print("part 2", total_part2)


if __name__ == "__main__":
    main()
