import re

lines = []
with open("input.txt") as file:
    for line in file:
        lines.append(line.strip())

pattern = re.compile(r"mul\((\d+),(\d+)\)")
products = []

for line in lines:
    products.extend(pattern.findall(line))

total_sum_1 = sum([int(pair[0]) * int(pair[1]) for pair in products])

combined_dump = "".join(lines)
first_section = re.split(r"don\'t\(\)", combined_dump)[0]
other_enabled_sections = re.findall(r"do\(\)(.*?)don\'t\(\)", combined_dump)

products_2 = []
for section in [first_section] + other_enabled_sections:
    products_2.extend(pattern.findall(section))

total_sum_2 = sum([int(pair[0]) * int(pair[1]) for pair in products_2])

print("part 1", total_sum_1)
print("part 2", total_sum_2)
