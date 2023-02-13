def is_odd_string(s1):
    if sum([ord(s) - 96 for s in s1]) % 2 == 0:
        return False
    return True

print(is_odd_string('aa'))