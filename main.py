import dynamic_programming as fibonachi

def result():
    i = 0
    inval = int(input("Введите значение переменной a :"))
    # print(i)
    while (inval>=fibonachi.fib(i)):
        i = i+1
        if fibonachi.fib(i) == inval:
            # print("Введенное число ")
            print("Введенное число = " + str(inval)+" в ряде Фибоначчи обнаружено!")
            print("Его номер в ряду = "+str(i+1))
            # print(i+1)
            break
        if fibonachi.fib(i) > inval:
            d1=fibonachi.fib(i) - inval
            d2 = inval - fibonachi.fib(i-1)
            # print(d1)
            # print(d2)
            print("Введенное число = " + str(inval) + " в ряде не обнаружено!")
            print("Ближайший меньший элемент ряда Фибоначчи = " + str(fibonachi.fib(i - 1)) + " его номер в ряду = " + str(i))
            print("Ближайший больший элемент ряда Фибоначчи = " + str(fibonachi.fib(i)) + " его номер в ряду = " + str(i + 1))
            if d1>d2:
                print("Наиболее близкий элемент ряда Фибоначчи = " + str(fibonachi.fib(i - 1)) + " его номер в ряду = " + str(i))
            else :
                print("Наиболее близкий элемент ряда Фибоначчи = " + str(fibonachi.fib(i)) + " его номер в ряду = " + str(i+1))

            # print("Введенное число ")

            # print(i+1)
            break

result()
