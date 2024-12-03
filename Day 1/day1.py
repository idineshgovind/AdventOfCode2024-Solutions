# part 1
lists = [[int(x) for x in line.split()] for line in open("input.txt")]
print("part 1", sum([abs(a - b) for a, b in zip(sorted([line[0] for line in lists]), sorted([line[1] for line in lists]))]))
# part 2
lists = [[int(x) for x in line.split()] for line in open("input.txt")]
list2 = [line[1] for line in lists]
print("part 2", sum([line[0] * list2.count(line[0]) for line in lists]))