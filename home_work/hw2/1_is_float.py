'''Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), 
и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения, 
вместо этого, необходимо повторно запросить у пользователя ввод данных.'''



def is_float():
    while True:
        try:
            value = float(input("Введите дробное число: "))
            return value
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")

is_float()