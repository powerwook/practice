n = str(input())
position = len(n) // 2
left = n[:position]
right = n[position:]

left_num = 0
right_num = 0

for x,y in zip(left,right):
    left_num += int(x)
    right_num += int(y)

if left_num == right_num:
    print("LUCKY")
else:
    print("READY")

