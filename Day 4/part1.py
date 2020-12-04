passports = open('in.txt').read().split('\n\n')
ans = 0
for passport in passports:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        ans += 1

print(ans)