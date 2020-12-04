f = open('in.txt')
arr = [s.split(':') for s in f.readlines()]
ans = 0
for i in arr:
    pref = i[0].split()
    counts = pref[0].split('-')
    char = pref[1]
    suffix = i[1].strip()
    x = int(counts[0]) - 1
    y = int(counts[1]) - 1
    if (suffix[x] == char and suffix[y] != char) or (suffix[x] != char and suffix[y] == char):
        ans += 1

print(ans)