S = input()
zero_len = S.split('0')
one_len = S.split('1')
print(zero_len)
print(one_len)
# 빈문자 리스트내에서 제거
zero_len = len([x for x in zero_len if x])
one_len = len([x for x in one_len if x])
if zero_len >= one_len:
    print(one_len)
else:
    print(zero_len)