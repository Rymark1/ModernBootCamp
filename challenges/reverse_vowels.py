def reverse_vowels(s1):
    values = [index for index, value in enumerate(s1) if value.lower() in "aeiou"]
    s1 = list(s1)
    # for i in range(len(values)):
    for i, val in enumerate(values):
        if i >= len(values) // 2:
            break
        idx1 = i
        idx2 = (i+1) * -1
        v1 = values[idx1]
        v2 = values[idx2]
        s1[v1], s1[v2] = s1[v2], s1[v1]
    return "".join(s1)


# def reverse_vowels(s1):
#     values = [index for index, value in enumerate(s1) if value.lower() in "aeiou"]
#     s1 = list(s1)
#     print(len(values))
#     for i in range(len(values)):
#         if i >= len(values) // 2:
#             break
#         s1[values[i]], s1[values[(i+1) * -1]] = s1[values[(i+1) * -1]], s1[values[i]]
#     return "".join(s1)


print(reverse_vowels("Hello!")) # "Holle!"
print(reverse_vowels("Tomatoes")) # "Temotaos"
print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"
print(reverse_vowels("aeiou")) # "uoiea"
print(reverse_vowels("why try, shy fly?")) # "why try, shy fly?"