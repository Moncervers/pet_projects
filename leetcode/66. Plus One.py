digits = [9, 9, 9, 9]

# SOLUTION 1
# result = int(''.join(map(str, digits)))
# result += 1
# result = list(str(result))
# for i in range(len(result)):
#     result[i] = int(result[i])
# print(result)

digits[-1] += 1
i = -1
while digits[i] == 10:
    digits[i] = 0
    try:
        digits[i - 1] += 1
        i -= 1
    except IndexError:
        digits.append(0)
        digits[0] = 1

print(digits)
