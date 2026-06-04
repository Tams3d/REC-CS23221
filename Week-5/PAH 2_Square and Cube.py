def count_vowels(string):
    vow = 0
    for ch in string:
        if ch.lower() in "aeiou":
            vow += 1
    return vow


input_string = input()
vowel_count = count_vowels(input_string)
print(f"Number of vowels in the string: {vowel_count}")
