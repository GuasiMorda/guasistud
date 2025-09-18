first_max = -1
second_max = -1

while True:
    user = int(input())
    if user == 0:
        break
    if user > first_max:
        second_max = first_max
        first_max = user
    elif user > second_max and user != first_max:
        second_max = user
print(second_max)