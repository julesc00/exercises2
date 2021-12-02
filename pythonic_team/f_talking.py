
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
    trans_word = [syl + f"f{syl[-1]}" for syl in word_split]
    return trans_word

print(two_ltr_word_trans("Hola"))

