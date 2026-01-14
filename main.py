import auth
import finance

def startApp():
    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Реєстрація")
        print("2. Вхід")
        print("3. Вихід")
        
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