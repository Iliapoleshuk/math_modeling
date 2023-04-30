a = int(input())
b = int(input())
if b == 0:
    print('нельзя')
elif a % b == 0 :
    print('делиться')
    print(a / b)
else:
    print(a % b)
    print(a / b)
