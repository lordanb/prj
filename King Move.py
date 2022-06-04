a = int(input())
b = int(input())
c = int(input())
if (a * b * c) % 2 == 0 and a % 2 != 0:
    print('YES')
elif (a * b * c) % 2 == 0 and b % 2 != 0:
    print('YES')
elif (a * b * c) % 2 == 0 and c % 2 != 0:
    print('YES')
else:
    print('NO')
