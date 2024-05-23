x = int(input())

for i in range(len(str(x)) // 2):
    if str(x)[i] != str(x)[-1 - i]:
        # return False
        print('Not Palindrome')
    # return True
    print('Palindrome')


str_x = str(x)
# return str_x == str_x[::-1]
print(str_x == str_x[::-1])