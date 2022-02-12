password = input('Введите пароль: ')
password2 = input('Повторите пароль: ')
while password2 != password:
    print("Введите пароль заново.")
    break
while password2 == password:
    print('Пароль введён верно.')
    break

