def f1(x, y=1, z=1):
    if x < 0 or type(x) != int:
        return "Эррор!!!"
    else:
        while z <= x:
            y *= z
            z += 1
        return "Факториал числа " + str(x) + " равен " + str(y)


print(f1(int(input("Введите число: "))))


def f2(x, y=1):
    if x < 0 or type(x) != int:
        return "Эррор!!!"
    if x in (0, 1):
        return "Факториал равен 1"
    while x > 0:
        y *= x
        x -= 1
    return "Факториал равен " + str(y)


a = int(input())

print(f2(a))


def f3(x, y=1):
    if x < 0 or type(x) != int:
        return "Эррор!!!"
    elif x == 0:
        return "Факториал 0 равен 1"
    else:
        for i in range(1, x+1):
            y *= i
        return "Факториал: " + str(y)


print(f3(int(input("Введите число: "))))


def factorial(x):
    if x in (0, 1):
        return 1
    return x * factorial(x - 1)


a = int(input("Введите чило: "))
print(factorial(a))

