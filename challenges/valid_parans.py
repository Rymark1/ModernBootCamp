def valid_parentheses(s1):
    start = end = 0
    if s1[0] == ")":
        return False

    for index,value in enumerate(s1):
        if value == "(":
            start = index
            for idx, val in enumerate(s1[start + 1::]):
                if val == ")":
                    end = idx + start + 1
                    break
            if start > end or end == 0:
                return False
    return True


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
print(valid_parentheses('))(('))
print(valid_parentheses('())('))
print(valid_parentheses('()()()()())()('))
print(valid_parentheses('(()))('))
#                        01234567890123
