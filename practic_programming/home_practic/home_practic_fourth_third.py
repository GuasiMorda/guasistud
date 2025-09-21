input_string = input()

words = input_string.split()

result_words = []
for word in words:
    if word == "кот":
        result_words.append("ток")
    else:
        result_words.append(word)

print(" ".join(result_words))