s = "   fly me   to   the moon  "

# SOLUTION 1
# temp = s.split()
# print(len(temp[-1]))

# SOLUTION 2
right_border = len(s) - 1
count = 0

while s[right_border] == " " and right_border >= 0:
    right_border -= 1

while s[right_border] != " " and right_border >= 0:
    count += 1
    right_border -= 1

print(count)
