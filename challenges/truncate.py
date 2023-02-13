def truncate(s1, n1):
    if n1 < 3:
        return "Truncation must be at least 3 characters."
    elif len(s1) > 3 and n1 <= len(s1):
        return s1[0:n1-3] + "..."
    else:
        return s1


print(truncate("Super cool", 2))
print(truncate("Super cool", 1))
print(truncate("Super cool", 0))
print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
print(truncate("Another test", 12))
print(truncate("Woah", 4))
print(truncate("Woah", 3))
print(truncate("Yo",100))
print(truncate("Holy guacamole!", 152))
