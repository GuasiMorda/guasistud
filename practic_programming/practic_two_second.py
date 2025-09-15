print("[1] Найти радиус круга")
print("[2] Найти площадь квадрата")
user_input_choice = int(input("Выберите действие: "))
user_input_number = int(input("Введите значение фигуры: "))
if user_input_choice == 1:
    print("Радиус круга: ", user_input_number / 2)
elif user_input_choice == 2:
    print("Площадь квадрата: ", user_input_number * user_input_number)
else:
    print("Других выборов нету!")