user_input = input()
count = 0
for char in user_input:
    if char.isdigit():
        count += 1

if count == 0:
    print("В строке нету цифр")
else:
    print(f"В строке {count} цифры")