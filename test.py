# Задание 12
##arr = [int(input())]
##while True:
##    num = int(input())
##    if num != 0:
##        arr.append(num)
##    else:
##        break
##loc_mx = []
##for i in range(1, len(arr)-1):
##    if arr[i-1] <= arr[i] >= arr[i+1]:
##       loc_mx.append(arr[i])
##is_Exist = False
##for i in loc_mx:
##    if i%2==0:
##        is_Exist = True
##        break
##print('существует' if is_Exist else 'не существует')


# Задание 15
##n = int(input())
##multy = 1
##arr = [x for x in range(1, n+1)]
##num_7 = [x for x in arr if x%7==0]
##for i in num_7:
##    multy *= i
##print(multy)


# Задание 17
#a)
##a = int(input())
##n = int(input())
##print(a**n)
#б)
##multy = 1
##for i in range(1, n+1):
##    multy *= (a+i-1)
##print(multy)
#в)
##sm = 0
##for i in range(0, n+1):
##    denom = 1
##    for j in range(n+1):
##        denom *= (a + j)
##    sm += 1/denom
##print(sm)
    

# Задание 19
##x = int(input())
##y = int(input())
##z = int(input())
##arr = [x,y,z]
##mx = max(arr)
##mn = min(arr)
##mdl = 0
##for i in arr:
##    if mn <= i <= mx:
##        mdl = i
##isExist = True
##if mx > (mn + mdl):
##    isExist = False
##if isExist:
##    print('Треугольник существует')
##    if mx**2 < (mn**2 + mdl**2):
##        print('Треугольник остроугольный')


# Задание 20
##x = int(input())
##y = int(input())
##z = int(input())
##arr = [x,y,z]
##if sum([x,y,z]) < 1:
##    min_i = arr.index(min(arr))
##    if min_i == 0:
##        x = (y + z)/2
##    elif min_i == 1:
##        y = (x + z)/2
##    else:
##        z = (y + x)/2
##else:
##    min_i = arr.index(min(arr[:2]))
##    if min_i == 0:
##        x = (y + z)/2
##    else:
##        y = (x + z)/2


# Задание 21
##a = int(input())
##b = int(input())
##c = int(input())
##disc = (b**2 - 4*a*c)**0.5
##print(disc)
##if disc == 0:
##    x = -b/(2*a)
##    print(f'Корень x - {x}')
##if disc > 0:
##    x1 = (-b + disc)/(2*a)
##    x2 = (-b - disc)/(2*a)
##    print(f'Корень x1 - {x1}, Корень x2 - {x2}')
##else:
##    print('Не имеет корней')


# Задание 22
##x = int(input())
##s = ''
##while x > 0:
##  s = str(x%2) + s
##  x //= 2
##print(int(s))
