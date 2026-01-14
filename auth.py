usersDatabase = {}

def registerUser():
    userLogin = input("Створіть логін: ")
    if userLogin in usersDatabase:
        print("Цей логін вже зайнятий.")
    else:
        password = input("Створіть пароль: ")
        usersDatabase[userLogin] = password
        print("Реєстрація успішна!")

def loginUser():
    userLogin = input("Логін: ")
    userPassword = input("Пароль: ")
    savedPassword = usersDatabase.get(userLogin)
    
    if savedPassword == userPassword and savedPassword is not None:
        print(f"\nВітаємо, {userLogin}!")
        return True
    else:
        print("Невірний логін або пароль.")
        return False