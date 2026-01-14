import coursesBudgets

financeTransactions = {}

def convertToBase(amount, currency):
    rate = coursesBudgets.exchangeRates.get(currency, 1.0)
    return amount / rate

def createBudgetTracker(categoryName, limitValue):
    currentSpent = 0
    
    def addExpense(amount):
        nonlocal currentSpent
        if currentSpent + amount > limitValue:
            print(f"\nНедостатньо коштів у бюджеті '{categoryName}'!")
            remaining = limitValue - currentSpent
            print(f"Залишилось: {remaining}. Спроба витратити: {amount}")
            return False 
        
        currentSpent = currentSpent + amount
        return True 
    
    return addExpense

budgetTrackers = {}
for category, limit in coursesBudgets.categoryBudgets.items():
    tracker = createBudgetTracker(category, limit)
    budgetTrackers[category] = tracker

def calculateTotalRecursive(transactionIds):
    if not transactionIds:
        return 0
    
    currentId = transactionIds[0]
    currentAmount = financeTransactions[currentId]['baseAmount']
    
    remainingIds = transactionIds[1:]
    totalOfRemaining = calculateTotalRecursive(remainingIds)
    
    return currentAmount + totalOfRemaining

def manageTransactions():
    while True:
        print("\n=== Керування фінансами ===")
        print("1. Додати транзакцію")
        print("2. Показати всі транзакції")
        print("3. Назад")
        
        choice = input("Оберіть дію: ")

        if choice == "1":
            try:
                tid = input("Введіть ID транзакції: ")
                amt = float(input("Сума: "))
                curr = input("Валюта (USD, EUR, UAH): ").upper()
                cat = input("Категорія (Їжа/Транспорт/Розваги): ")

                if curr not in coursesBudgets.exchangeRates:
                    print(f"Валюта '{curr}' не підтримується.")
                elif cat not in coursesBudgets.categoryBudgets:
                    print(f"Категорії '{cat}' не існує.")
                else:
                    baseAmt = convertToBase(amt, curr)
                    if budgetTrackers[cat](baseAmt):
                        financeTransactions[tid] = {
                            "amount": amt, 
                            "currency": curr,
                            "baseAmount": baseAmt, 
                            "category": cat
                        }
                        print("Запис успішно додано!")
                    else:
                        print("Запис НЕ збережено.")
            except ValueError:
                print("Будь ласка, вводьте цифри для суми!")

        elif choice == "2":
            if not financeTransactions:
                print("Список транзакцій порожній.")
            else:
                for tid, info in financeTransactions.items():
                    print(f"ID {tid}: {info['amount']} {info['currency']} ({info['category']})")
                total = calculateTotalRecursive(list(financeTransactions.keys()))
                print(f"Загальна сума: {total} USD")

        elif choice == "3":
            break