def letter_counter(s1):
    letter_counter.count = 0

    def inner(l1):
        return s1.lower().count(l1)

    return inner


counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i')) # 2
print(counter2('t')) # 1