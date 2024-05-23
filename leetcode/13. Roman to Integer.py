# 35ms, 16,4 MB
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,}
#         i = 0
#         sum = 0
#         prev_self = 0
#
#         for self in reversed(s):
#              if prev_self > roman_symbol[self]:
#                 sum -= roman_symbol[self]
#              else:
#                 sum += roman_symbol[self]
#                 prev_self = roman_symbol[self]
#         return sum

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# 42 ms, 16,5 MB
num_dict = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
# s = input()
# s = "LVIII"
s = "MCMXCIV"

result = num_dict[s[0]]
temp = 0

for i in range(1, len(s)):
    result += num_dict[s[i]]
    if num_dict[s[i - 1]] < num_dict[s[i]]:
        temp += num_dict[s[i - 1]]

print(result - temp * 2)
