import re

# Запрашиваем данные у пользователя
input_string = input("Введите данные через пробел в порядке: фамилия, имя, отчество, дата рождения dd.mm.yyyy, номер телефона и пол: ")
input_list = input_string.split()

# Проверяем количество данных
if len(input_list) != 6:
    print("Ошибка: неверное количество данных")
else:
    # Разбираем данные на составляющие
    last_name = input_list[0]
    first_name = input_list[1]
    middle_name = input_list[2]
    birth_date = input_list[3]
    phone_number = input_list[4]
    gender = input_list[5]
    
    # Проверяем формат даты рождения
    if not re.match(r'\d{2}.\d{2}.\d{4}', birth_date):
        print("Ошибка: неверный формат даты рождения (dd.mm.yyyy)")
    else:
        # Проверяем формат номера телефона
        if not phone_number.isdigit():
            print("Ошибка: номер телефона должен быть целым беззнаковым числом")
        else:
            # Проверяем формат пола
            if gender not in ['m', 'f']:
                print("Ошибка: пол должен быть обозначен буквой 'm' или 'f'")
            else:
                # Записываем данные в файл
                with open(f"{last_name}.txt", "a") as f:
                    f.write(f"{last_name} {first_name} {middle_name} {birth_date} {phone_number} {gender}\n")
                print("Данные успешно записаны в файл")