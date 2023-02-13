def vowel_count(s1):
    vowels = {}
    for letter in s1:
        letter = letter.lower()
        if letter in 'aeiou':
            if letter in vowels:
                vowels[letter] = vowels.pop(letter) + 1
            else:
                vowels[letter] = 1
    return vowels


def vowel_count(s1):
    s1 = s1.lower()
    return {letter: s1.count(letter) for letter in s1 if letter in "aeiou"}


print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))
