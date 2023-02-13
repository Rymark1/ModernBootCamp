def min_max_key_in_dictionary(d1):
    key_values = list(sorted((d1.keys())))
    return [key_values[0], key_values[-1]]


print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'})) # [1,10]
print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"})) # [1,4]