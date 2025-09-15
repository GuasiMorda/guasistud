user_input_wight = float(input("Введите вес: "))
user_input_growth = float(input("Введите рост (Метры): "))
imt = (user_input_wight / user_input_growth ** 2)

if imt <= 18.5:
    print("Дефицит массы тела")
elif imt >= 18.6 and imt <= 24.9:
    print("Нормальный вес")
elif imt >= 25 and imt <= 29.9:
    print("избыточная масса тела")