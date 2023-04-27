def printSum(a: int, b: int) -> None:
    print(a + b)

try:
    a = 90
    b = 3
    print(a // b)
    printSum(23, 234)
    abc = [1, 2]
    abc[3] = 9
except TypeError as e:
    print("Нельзя выполнять операции с объектами разных типов!", )
except IndexError as e:
    print("Массив выходит за пределы своего размера!")
except ZeroDivisionError as e:
        print("На ноль делить нельзя!")