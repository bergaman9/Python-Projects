def spin_words(sentence):
    words = sentence.split()
    list = []
    for word in words:
        if len(word) > 5:
            list.append("".join(reversed(word)))
        else:
            list.append(word)

    return " ".join(list)
            

print(spin_words("Bu bir deneme yazısıdır"))