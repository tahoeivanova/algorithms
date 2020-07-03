import math
# 03 July 2020
# написать функцию линейного поиска
# 20.45
# 20.54
def linear_search(a:list, value:int):
    '''
    Функция осуществляет линейный поиск по массиву. Принимает на вход
    список и значение int, возвращает индекс первого вхождения значения. Если значения нет,
    возвращает -1.
    '''
    N = len(a)
    for i in range(N):
        if a[i] == value:
            return i
    return -1

def test_linear_search():
    a = [1,2,3,4,5]
    result = linear_search(a, 3)
    print(f'Тетсирование функции {linear_search.__name__}')
    # print(f'Описание функции: {linear_search.__doc__}')
    if result == 2:
        print('Test 1 OK')
    else:
        print('Test 1 FAIL')

    a = [1,2,3,4,5]
    result = linear_search(a, 6)
    if result == -1:
        print('Test 2 OK')
    else:
        print('Test 2 FAIL')

# инверсия массива
# 20:58
# 21:07
def invert_array(a:list):
    '''
    Инверсия массива
    '''
    N = len(a)
    for i in range(N//2):
        a[i],a[N-i-1] = a[N-i-1], a[i]

def test_invert_array():
    a = [1, 2, 3, 4, 5]
    invert_array(a)
    print(f'\nТетсирование функции {invert_array.__name__}')
    # print(f'Описание функции: {invert_array.__doc__}')
    if a == [5,4,3,2,1]:
        print('Test 1 OK')
    else:
        print('Test 1 FAIL')

# Циклический сдвиг влево
# 21:09
def cycle_array_left(a:list): #[1,2,3,4,5] -> [2,3,4,5,1]
    N = len(a)
    tmp = a[0]
    for k in range(N-1):
        a[k]= a[k+1]
    a[N-1] = tmp

def test_cycle_array_left():
    a = [1,2,3,4,5]
    cycle_array_left(a)
    print(f'\nТетсирование функции {cycle_array_left.__name__}')
    if a == [2,3,4,5,1]:
        print('Test 1 OK')
    else:
        print('Test 1 FAIL')
# 21.16
def cycle_array_right(a:list): # [1,2,3,4,5] -> [5,1,2,3,4]
    N = len(a)
    tmp = a[N-1]
    for k in range(N-2, -1,-1):
        a[k+1] = a[k]
    a[0]=tmp

def test_cycle_array_right():
    a = [1,2,3,4,5]
    cycle_array_right(a)
    print(f'\nТетсирование функции {cycle_array_right.__name__}')

    if a == [5,1,2,3,4]:
        print('Test 1 OK')
    else:
        print('Test 1 FAIL')

# 23 05 - 23 14
# Решето Эратосфена
def eratosphen(n:int):
    '''
    Решето Эратосфена
    :param n: до какого числа считать простые числа
    :return: множество простых чисел до n включительно
    '''
    a = list(range(0,n+1))
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <=n:
                a[j] = 0
                j += i
        i += 1
    a = set(a)
    a.remove(0)
    return a




def test_eratosphen():
    print(eratosphen.__doc__)
    assert eratosphen(10) == {2,3,5,7}


# 23 18 - 23 22
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    i = 2
    limit = math.sqrt(n)
    while i <= limit:
        if n % i == 0:
            return False
        i +=1
    return True

def test_is_prime():
    assert is_prime(101) == True


def sort_insert(a):
    '''
    Сортировка вставками
    '''
    N = len(a)
    for top in range(1, N):
        k = top
        while k > 0 and a[k-1]>a[k]:
            a[k-1], a[k] = a[k], a[k-1]
            k -= 1

def test_sort_insert():
    a = [1,5,2,3,6]
    sort_insert(a)
    assert a == [1,2,3,5,6]

    a = [1,-5, 2,-3,6]
    sort_insert(a)
    assert a == [-5,-3,1,2,6]

# 23 48 - 23 54
def sort_choice(a):
    '''
    Сортировка методом выбора
    '''
    N = len(a)
    for pos in range(N-1):
        for k in range(pos+1, N):
            if a[k]<a[pos]:
                a[pos], a[k] = a[k], a[pos]


def test_sort_choice():
    a = [1,3,0,1,-1, 5]
    sort_choice(a)
    assert a == [-1,0,1,1,3,5]

def bubble_search(a):
    N = len(a)
    for i in range(N-1):
        for j in range(N - i -1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def test_bubble_search():
    a = [1, 3, 0, 1, -1, 5]
    bubble_search(a)
    assert a == [-1, 0, 1, 1, 3, 5]

def count_sort(n):
    '''
    На вход подается число вводимых цифр от 0 до 9.
    Цифры сортируются методом подсчета.
    '''
    F = [0]*n
    for i in range(n):
        try:
            x = int(input('Введите число от 0 до 9: '))
        except:
            print('Вы ввели не число')
        F[x] += 1

    result_list = []
    for i in range(n):
        result_list += ([i]*F[i])
    return result_list

# пример рекурсии
def matroshka(n):
    if n == 1:
        print('Матрешечка')
    else:
        print('Верх матрешки n = ', n)
        matroshka(n-1)
        print('Низ матрешки n = ', n)

# факториал
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def test_factorial():
    assert factorial(6)==720

# факториал рекурентный
def factorial_recursion(n):
    assert n >= 0 , 'Факториал отрицательных не определен'
    if n == 0:
        return 1
    else:
        return factorial_recursion(n-1)*n

def test_factorial_recursion():
    assert factorial_recursion(6)==720

# алгоритм Евклида - нахождение НОД
def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)

def towers(n,towerFrom, towerTo,towerWith):
    if n >= 1:
        towers(n-1, towerFrom, towerWith, towerTo)
        print(f' {n} Перемещен с {towerFrom} на {towerTo}')
        towers(n-1, towerWith, towerTo, towerFrom)
# 00:48 - 00:53
def degree_simple(a,n):
    if n == 0:
        return 1
    else:
        degree = 1
        for i in range(1, n+1):
            degree *= a
    return degree

def degree_rec(a,n):
    if n == 0:
        return 1
    else:
        return degree_rec(a,n-1)*a

def test_degree_simple():
    assert degree_simple(2,10) == 1024

def test_degree_rec():
    assert degree_rec(2,10) == 1024


'''
gcd - greatest common devisor,
lcm - least common multiple
'''
# НОК
def lcm(a,b):
    m = a * b
    # сначала найдем НОД
    while a!=0 and b!=0:
        if a>b:
            # a = a%b
            a%=b
        else:
            b%=a
    return m//(a+b)

# фибоначчи без рекурсии
def finonacci_simple(n):
    fib1 = fib2 = 1
    i = 2
    while i < n:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i+=1
    return fib2

# фибоначчи с рекурсией
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# фибоначчи lambda
fib_num = lambda n: fib_num(n-1) + fib_num(n-2) if n>2 else 1



if __name__ == '__main__':
    test_linear_search()
    test_invert_array()
    test_cycle_array_left()
    test_cycle_array_right()
    # print(count_sort(10))
    matroshka(4)
    print(gcd(120,100))
    towers(3, 'A','B','C')
    print(lcm(5,4))
    print(finonacci_simple(10))
    print(fibonacci(10))
    print(fib_num(10))

# 01:28
