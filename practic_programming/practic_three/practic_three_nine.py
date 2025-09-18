max_number = 0
count_max = 0

while True:
    user = int(input())
    if user == 0:
        break
    if user > max_number:
        max_number = user
        count_max = 1
    elif user == max_number:
        count_max += 1
print(count_max)