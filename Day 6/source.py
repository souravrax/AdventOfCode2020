groups=open('in.txt').read().split('\n\n')

part2 = 0
def solve(group):
    global part2
    peoples = group.split('\n')
    d = {}
    for people in peoples:
        for question in people:
            d.setdefault(question, 0)
            d[question] += 1
    
    print(len(peoples))
    for k in d:
        if d[k] == len(peoples):
            part2 += 1
    return len(d)


part1 = 0
for group in groups:
    part1 += solve(group)

print(part1)
print(part2)