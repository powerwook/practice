s = input()
result = 0

for i in s:
    if result == 0 or i == '0':
        result += int(i)
    else:
        result *= int(i)
print(result)