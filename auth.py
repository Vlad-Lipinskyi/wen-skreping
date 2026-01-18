usersDatabase = {}

def registerUser():
    login = input("Створіть логін: ")
    if login in usersDatabase:
        print("Цей логін вже зайнятий.")
    else:
        password = input("Створіть пароль: ")
        usersDatabase[login] = password
        print("Реєстрація успішна!")

def loginUser():
    login = input("Логін: ")
    password = input("Пароль: ")

    if usersDatabase.get(login) == password:
        print(f"\nВітаємо, {login}!")
        return True
    else:
        print("Невірний логін або пароль.")
        return False
