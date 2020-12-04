passports = open('in.txt').read().split('\n\n')
ans = 0


def hcl_validate(string):
    if string.count("#") != 1:
        return False
    string = string[1:]
    # print(string)
    for i in string:
        if i.isalpha():
            if ord(i) > ord('f') or ord(i) < ord('a'):
                return False
        elif i.isdigit():
            continue
        else:
            return False

    return True

for passport in passports:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        pairs = passport.split()
        flag = True
        for pair in pairs:
            k, v = pair.split(':')
            if (len(v) == 0):
                flag = False
                break
            # print(k, v)
            if k == "byr":
                if len(v) != 4 or int(v) < 1920 or int(v) > 2002:
                    flag = False
            elif k == "iyr":
                if len(v) != 4 or int(v) < 2010 or int(v) > 2020:
                    flag = False
            elif k == "eyr":
                if len(v) != 4 or int(v) < 2020 or int(v) > 2030:
                    flag = False
            elif k == "hgt":
                t = v[-2:]
                v = v[:-2]
                if len(v) == 0:
                    flag = False
                    break
                val = int(v)
                # print(t, val);
                if t == "cm":
                    if val < 150 or val > 193:
                        flag = False
                elif t == "in":
                    if val < 59 or val > 76:
                        flag = False
                else:
                    flag = False

            elif k == "hcl":
                if not hcl_validate(v):
                    flag = False
            elif k == "ecl":
                colors = ['amb','blu','brn','gry','grn','hzl','oth']
                if not v in colors:
                    flag = False
            elif k == "pid":
                if len(v) != 9:
                    flag = False

        if flag:
            ans += 1

print(ans)
