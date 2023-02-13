def once(func):
    once.run = False

    def inner(*args):
        if not once.run:
            once.run = True
            return func(*args)

    return inner


def add(a, b):
    return a + b


oneAddition = once(add)

print(oneAddition(2, 2))  # 4
print(oneAddition(2, 2))  # None
print(oneAddition(12, 200))  # None