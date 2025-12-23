import hashlib

usersDataBase = [{"username": "kleryxx", "password": "qwerty"}]

def askLogin():
    print("-- Вхід у систему!")
    inputLogin = input("Введіть логін: ")
    inputPassword = input("Введіть пароль: ")

    isRight = False

    for user in usersDataBase:
        if user["username"] == inputLogin and user["password"] == inputPassword:
            isRight = True

        if isRight == True:
            print(f"Вітаємо {inputLogin}!")
        else:
            print("Помилка: логін або пароль не вірний")


# askLogin()


def registration():
    print("-- Реєстрація користувача!")
    createUsername = input("Придумайте логін: ")

    isUsernameUse = False
    for user in usersDataBase:
        if user["username"] == createUsername:
            isUsernameUse = True

    try:
        if isUsernameUse == True:
            print("Логін вже занятий. Спробуйте інший")
        else:
            createPassword = input("Придумайте пароль: ")
            newUser = {"username": createUsername, "password": createPassword}
            usersDataBase.append(newUser)
            print(f"Користувач {createUsername} зареєстровано!")
    except UnboundLocalError:
        print("Логін вже занятий. Спробуйте інший")

# registration()

# def hashPassword(password):
#     hashedPassword = hashlib.sha256(password.encode()).hexdigest()
#     print(password)
#     return hashedPassword

