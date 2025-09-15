user_input = int(input("Введите цифру: "))
print("Таблица умножения: ")
for i in range(1, 11):
    result = user_input * i
    print(user_input, i, result)