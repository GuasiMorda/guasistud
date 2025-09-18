count = 0

while True:
    user = int(input())
    if user == 0:
        break
    if user % 2 == 0:
        count += 1
print(count)