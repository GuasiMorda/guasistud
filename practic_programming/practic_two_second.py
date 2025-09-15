print("[1] Найти радиус круга")
print("[2] Найти площадь квадрата")
user_input_choice = int(input("Выберите действие: "))
user_input_number = int(input("Введите значение фигуры: "))
if user_input_choice == 1:
    print("Радиус круга: ", user_input_number / 2)
else:
    print("Площадь квадрата: ", user_input_number * user_input_number)
