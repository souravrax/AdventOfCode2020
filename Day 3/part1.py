mp = open('in.txt').readlines()
length = mp[0].count('#') + mp[0].count('.')
def get(many, how):
    ans = 0
    index = 0
    for i in range(0, len(mp), how):
        index %= length
        if mp[i][index] == '#':
            ans += 1
        index += many

    return ans

print(get(1,1) * get(3, 1) * get(5, 1) * get(7, 1) * get(1, 2))