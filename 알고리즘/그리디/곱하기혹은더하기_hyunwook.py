s = input()
result = 0
# 숫자 1일경우 더해주는게 이득
for i in s:
    if result <= 1 or i == '0' or i == '1':
        result += int(i)
    else:
        result *= int(i)
print(result)