# s = input()
# s = "()[]{}"
s = "(]"

# TODO not working
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False

        dumb_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for i in range(0, len(s), 2):

            if s[i] != dumb_dict[s[i + 1]]:
                return False

        return True


print(Solution().isValid(s))
