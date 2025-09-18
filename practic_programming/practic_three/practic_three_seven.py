prev = None
count = 0

while True:
    user = int(input())
    if user == 0:
        break
    if prev is not None and user > prev:
        count += 1
    prev = user
print(count)