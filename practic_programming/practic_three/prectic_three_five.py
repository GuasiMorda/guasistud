prev = None
current = 0
max_count = 0

while True:
    num = int(input())
    if num == 0:
        break
    if num == prev:
        current += 1
    else:
        current = 1
    if current > max_count:
        max_count = current
    prev = num
print(max_count)