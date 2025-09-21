user_input = input("Введите текст: ")

count = {}

for i in user_input:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

result = ''
for i, count in count.items():
    result += f"{i}{count}"

print("Результат сжатия строки:", result)