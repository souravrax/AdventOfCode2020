f = open('in.txt')
arr = [s.split(':') for s in f.readlines()]
ans = 0
for i in arr:
    pref = i[0].split()
    cnts = pref[0].split('-')
    char = pref[1]
    suff = i[1].strip()
    cnt = suff.count(char)
    if cnt >= int(cnts[0]) and cnt <= int(cnts[1]):
        ans += 1

print(ans)