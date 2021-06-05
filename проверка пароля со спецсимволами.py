"""
проверка пароля
но для PC обработать строку сложнее, чем обработать число
потому можно загнать в число (но оно будет криво работать если просто
загнать в Int)
"""
#Task 1 пример 1
"""
password = input('введите пароль \n')
doublepass = input('введите пароль \n')
if password == doublepass:
    print ('ok')
else:
    print ('no')
"""
# Task 2 пример 2 сложный пароль
# нужны проверка длины, заглавные бквы, числа и спецсимволы
password = input('введите пароль \n')
if len(password) >= 8:
    pass 
else:
    print('короткий пароль, меньше 8 символов')
if password.islower() == True:
    print('нужны заглавные буквы')
if password.isalnum() == True:
    print('нужны особые символы')
else:
    print ('нужны цифры')
# if password.isnumeric() != True: #тоже вариант, он проверяет строку на циф
                                   #и буквы
#         print('нужны цифры и буквы в строке')
if "@" in password or "+" in password or "-" in password:
    print('ваш пароль хороший')
else:
    print ('нужны спецсимволы: @, +, -')
