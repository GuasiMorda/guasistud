print("Выберите режим конвертации валюты:\n" \
"[1] Рубль -> Доллар\n" \
"[2] Доллар -> Рубль")

user_input_choice = int(input("Введите: "))

if user_input_choice == 1:
    user_input_money = float(input("Введите кол-во денег: "))
    print(user_input_money / 82.63, "Долларов")
elif user_input_choice == 2:
    user_input_money = float(input("Введите кол-во денег: "))
    print(user_input_money * 82.63, "Рублей")
elif user_input_choice >= 3:
    print("Error")
