grid = {row_index + col_index * 1j: cell
        for row_index, row in enumerate(open('input.txt'))
        for col_index, cell in enumerate(row.strip())}

start_position = min(position for position in grid if grid[position] == '^')


def traverse(grid):
    current_position = start_position
    direction = -1
    visited_positions = set()

    while current_position in grid and (current_position, direction) not in visited_positions:
        visited_positions.add((current_position, direction))
        if grid.get(current_position + direction) == "#":
            direction *= -1j
        else:
            current_position += direction

    visited_cells = {position for position, _ in visited_positions}
    is_cycle_detected = (current_position, direction) in visited_positions
    return visited_cells, is_cycle_detected


path_visited = traverse(grid)[0]

cycles_detected = sum(traverse(grid | {obstructed_position: '#'})[1]
                      for obstructed_position in path_visited)

print("part 1", len(path_visited))
print("part 2", cycles_detected)
