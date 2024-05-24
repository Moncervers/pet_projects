# haystack = "sadbutsad"
# needle = "sad"
# haystack = "leetcode"
# needle = "leeto"
haystack = "hello"
needle = "ll"
# print(haystack.find(needle)) # too easy

for i in range(len(haystack)):
    # print(f'i = {i}, needle length = {len(needle)} haystack slice = {haystack[i:i+len(needle)]})
    # print(haystack[i:len(needle)])
    if haystack[i:i+len(needle)] == needle:
        print(i)
print(-1)
