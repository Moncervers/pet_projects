a = input()
b = input()
aL, bL = -len(a), -len(b)
i, carry, res = -1, 0, ""

while i >= aL or i >= bL:
    aBit = int(a[i]) if i >= aL else 0
    bBit = int(b[i]) if i >= bL else 0

    sum = aBit + bBit + carry
    res = str(sum % 2) + res
    carry = sum // 2

    i -= 1

print("1" + res if carry else res)
# todo Переделать
