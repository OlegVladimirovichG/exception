 # Если необходимо, исправьте данный код
def list_dev(array):
    try:
        d = 0
        exceptedRes1 = array[8] / 0
        print("exceptedRes1 =", exceptedRes1)
    except ZeroDivisionError as e:
        print("Exception:", e)
    except IndexError as e:
        print("Exception:", e)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list_dev(list)