import sys
from itertools import product
from operator import add, mul, concat


def is_solvable(target_value, numbers, include_concat=False):
    operations = (
        product([add, mul], repeat=len(numbers) - 1)
        if not include_concat
        else product([add, mul, concat], repeat=len(numbers) - 1)
    )
    for operation_set in operations:
        current_value = 0
        for index in range(len(numbers) - 1):
            operation, first_operand, second_operand = (
                operation_set[index],
                numbers[index] if index == 0 else current_value,
                numbers[index + 1],
            )
            current_value = (
                int(concat(str(first_operand), str(second_operand)))
                if operation == concat
                else operation(first_operand, second_operand)
            )
        if current_value == target_value:
            return True
    return False


input_data = open("input.txt").read().strip()

part1_result = part2_result = 0
for line in input_data.split("\n"):
    target_value = int(line.split(": ")[0])
    number_list = [int(n) for n in line.split(": ")[1].split(" ")]
    part1_result += target_value if is_solvable(target_value, number_list) else 0
    part2_result += target_value if is_solvable(target_value, number_list, True) else 0

print("part 1", part1_result)
print("part 2", part2_result)
