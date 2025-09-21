input_user = input("Введите строку: ").lower()

word = input_user.split()

unique_word = set(word)

print(" ".join(unique_word))
