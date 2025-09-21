input_user = input("Введите текст: ").lower()

word = input_user.split()

unique_word = set(word)

print(" ".join(unique_word))
