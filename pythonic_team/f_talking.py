
def word_splitter_in_2(msg: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    msg_split = [x for x in msg.split(" ")]
    word_split = []
    for word in msg_split:
        for idx in range(0, len(word), 2):
            word_split.append(word[idx:idx+2])
    print(word_split)
    print(msg_split)
    msg_trans = []


word_splitter_in_2("Hola me llamo jose")

