import auth
import finance
from colorama import Fore, Style, init
init() 

def startApp():
    while True:
        print(Fore.RED + "\n=== ГОЛОВНЕ МЕНЮ ===")
        print(Fore.CYAN + "1. Реєстрація")
        print(Fore.YELLOW + "2. Вхід")
        print(Fore.MAGENTA + "3. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            auth.registerUser()
        elif choice == "2":
            if auth.loginUser():
                finance.manageTransactions()
        elif choice == "3":
            print("Програма завершена. До побачення!")
            break

startApp()




## Додати операції: 
# 1. Видалення транзакції та редагування
# 2. Генерація звітів(виведення всіх транзакцій у файл)
# 3. Додати можливість обрати період звіту
# 4. Порахувати витрати за певний проміжок часу
# 5. Проглянути пакет coloram та використати в проєкті
## Не обов'язкове
# 6. Змінна паролю користувача(для підтверждення потрібен старий пароль)(погратися з хешуванням)
# 7. Пошук транзакції за датою або категорією