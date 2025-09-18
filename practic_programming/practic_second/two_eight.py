user_input_first = float(input("Введите первое число: "))
user_input_second = float(input("Введите второе число: "))
user_input_third = float(input("Введите третье число: "))

minimum = min(user_input_first, user_input_second, user_input_third)
maximum = max(user_input_first, user_input_second, user_input_third)

print("Максимальное число: ", maximum)
print("Минимальное число: ", minimum)
5