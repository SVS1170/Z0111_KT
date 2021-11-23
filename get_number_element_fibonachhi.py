i=0

def pow(x, n, I, mult):
    """
    Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая 
    перемножается с mult, а n – положительное целое
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    """Возвращает единичную матрицу n на n"""
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]


def fib(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]

def result(i):
    inval = int(input("Введите значение переменной a :"))
    # print(i)
    while (inval>=fib(i)):
        i = i+1
        if fib(i) == inval:
            # print("Введенное число ")
            print("Введенное число = " + str(inval)+" в ряде Фибоначчи обнаружено!")
            print("Его номер в ряду = "+str(i+1))
            # print(i+1)
            break
        if fib(i) > inval:
            d1=fib(i) - inval
            d2 = inval - fib(i-1)
            # print(d1)
            # print(d2)
            print("Введенное число = " + str(inval) + " в ряде не обнаружено!")
            print("Ближайший меньший элемент ряда Фибоначчи = " + str(fib(i - 1)) + " его номер в ряду = " + str(i))
            print("Ближайший больший элемент ряда Фибоначчи = " + str(fib(i)) + " его номер в ряду = " + str(i + 1))
            if d1>d2:
                print("Наиболее близкий элемент ряда Фибоначчи = " + str(fib(i - 1)) + " его номер в ряду = " + str(i))
            else :
                print("Наиболее близкий элемент ряда Фибоначчи = " + str(fib(i)) + " его номер в ряду = " + str(i+1))

            # print("Введенное число ")

            # print(i+1)
            break

result(i)
