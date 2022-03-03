def eat_vowels():
    word_without_vowels = []
    user_input = input("Enter a word: ").upper()
    for ltr in user_input:
        if ltr in "AEIOU":
            continue
        word_without_vowels.append(ltr)
    return "".join(word_without_vowels)


print(eat_vowels())
