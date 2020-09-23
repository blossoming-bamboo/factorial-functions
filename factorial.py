def f1(x, y=1, z=1):
    if x < 0:
        print("Число должно быть неотрицательным!")
    else:
        while z <= x:
            y *= z
            z += 1
        print("Факториал числа", x, "равен", y)


f1(int(input("Введите число: ")))


def f2(x, y=1):
    if x < 0:
        print("Число должно быть неотрицательным!")
    elif x == 0:
        print("Факториал 0 равен 1")
    else:
        while x > 0:
            y *= x
            x -= 1

        print("Факториал равен", y)


f2(int(input("Введите число: ")))


def f3(x, y=1):
    if x < 0:
        print("Число должно быть неотрицательным!!")
    else:
        for i in range(1, x+1):
            y *= i
        print("Факториал:", y)


f3(int(input("Введите число: ")))
