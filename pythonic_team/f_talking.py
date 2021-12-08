
# def efe_lang_translator(msg: str):
#     vowels = ["a", "e", "i", "o", "u"]
#     msg_split = [x for x in msg.split(" ")]
#     word_split = []
#     trans_word = []
#     trans_msg = []
#     for word in msg_split:
#         for idx in range(0, len(word), 2):
#             word_trans = word[idx:idx+2]
#             word_split.append(word_trans)
#
#     print(word_split)
            # for syl in word_split:
            #     if syl.endswith("a") or syl.endswith("e") or syl.endswith("i") or syl.endswith("o") or syl.endswith("u"):
            #         trans_word = syl + f"f{syl[-1]}"


# efe_lang_translator("Hola me como taco")


def two_ltr_word_trans(word):
    n = 2
    word_split = [word[idx:idx+n] for idx in range(0, len(word), n)]
    trans_word_starts_w_vow = []
    trans_word = [syl + f"f{syl[-1]}" for syl in word_split]


    return [trans_word]


print(two_ltr_word_trans("mañana"))


def three_ltr_word_starts_w_vowel(word):
    vowels = "aeiou"
    word_split = [word[0], word[1:]]
    trans_word = [syl + f"f{syl[0]}" if syl[0] in vowels else syl + f"f{syl[-1]}" for syl in word_split]
    print(trans_word)


three_ltr_word_starts_w_vowel("uno")


def three_ltr_word_ends_w_consonant(word):
    word_split = [word[:2], word[-1]]
    trans_word = [syl if len(syl) == 2 else f"f{word_split[0][1]}" + syl for syl in word_split]
    print(trans_word)


three_ltr_word_ends_w_consonant("quien")


def two_ltr_syl_w_ll(word):
    vowels = "aeiou"
    n = 2
    word_split = [word[idx:idx + n] for idx in range(0, len(word), n)]
    special_syl = [syl + f"{word_split[1][0]}f{word_split[1][0]}" if vowels not in syl else syl + f"f{syl[-1]}" for syl in word_split]
    print(special_syl)


two_ltr_syl_w_ll("corroborar")
