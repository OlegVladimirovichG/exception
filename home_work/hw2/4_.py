'''Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку. 
Пользователю должно показаться сообщение, что пустые строки вводить нельзя.'''

def empty_string():
    try:
        user_input = input("Введите что-нибудь: ")
        if not user_input:
            raise Exception("Пустые строки вводить нельзя!")
    except Exception as ex:
        print(ex)
    return print(user_input)
        
empty_string()