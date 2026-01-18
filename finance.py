import coursesBudgets
from datetime import datetime

financeTransactions = {}

def convertToBase(amount, currency):
    return amount / coursesBudgets.exchangeRates[currency]

def createBudgetTracker(category, limit):
    spent = 0

    def add(amount):
        nonlocal spent
        if spent + amount > limit:
            print(f"Перевищено бюджет категорії '{category}'")
            return False
        spent += amount
        return True

    def remove(amount):
        nonlocal spent
        spent -= amount
        if spent < 0:
            spent = 0

    return add, remove

budgetTrackers = {}
for cat, limit in coursesBudgets.categoryBudgets.items():
    add, remove = createBudgetTracker(cat, limit)
    budgetTrackers[cat] = {"add": add, "remove": remove}

def calculateTotalRecursive(ids):
    if not ids:
        return 0
    return financeTransactions[ids[0]]["baseAmount"] + calculateTotalRecursive(ids[1:])

def generateReport(filename="report.txt"):
    if not financeTransactions:
        print("Немає транзакцій для звіту.")
        return

    with open(filename, "w", encoding="utf-8") as file:
        file.write("ФІНАНСОВИЙ ЗВІТ\n")
        file.write(f"Дата створення: {datetime.now()}\n")

        for tid, t in financeTransactions.items():
            line = (
                f"ID: {tid} | "
                f"{t['amount']} {t['currency']} | "
                f"Категорія: {t['category']} | "
                f"USD: {round(t['baseAmount'], 2)}\n"
            )
            file.write(line)

        total = calculateTotalRecursive(list(financeTransactions.keys()))
        file.write("-" * 40 + "\n")
        file.write(f"ЗАГАЛЬНА СУМА: {round(total, 2)} USD\n")

    print(f"Звіт успішно збережено у файл '{filename}'")

def manageTransactions():
    while True:
        print("\n=== КЕРУВАННЯ ФІНАНСАМИ ===")
        print("1. Додати транзакцію")
        print("2. Показати всі транзакції")
        print("3. Видалити транзакцію")
        print("4. Редагувати транзакцію")
        print("5. Згенерувати звіт у файл")
        print("6. Назад")

        choice = input("Оберіть дію: ")

        if choice == "1":
            try:
                tid = input("ID транзакції: ")
                amt = float(input("Сума: "))
                curr = input("Валюта (USD/EUR/UAH): ").upper()
                cat = input("Категорія(Їжа/Транспорт/Розваги): ")

                if curr not in coursesBudgets.exchangeRates:
                    print("Невідома валюта.")
                    continue
                if cat not in coursesBudgets.categoryBudgets:
                    print("Невідома категорія.")
                    continue

                base = convertToBase(amt, curr)
                if budgetTrackers[cat]["add"](base):
                    financeTransactions[tid] = {
                        "amount": amt,
                        "currency": curr,
                        "baseAmount": base,
                        "category": cat
                    }
                    print("Транзакцію додано.")
            except ValueError:
                print("Некоректна сума.")

        elif choice == "2":
            if not financeTransactions:
                print("Транзакцій немає.")
            else:
                for tid, t in financeTransactions.items():
                    print(f"{tid}: {t['amount']} {t['currency']} ({t['category']})")
                total = calculateTotalRecursive(list(financeTransactions.keys()))
                print(f"Загалом: {round(total, 2)} USD")

        elif choice == "3":
            tid = input("ID для видалення: ")
            if tid in financeTransactions:
                t = financeTransactions[tid]
                budgetTrackers[t["category"]]["remove"](t["baseAmount"])
                del financeTransactions[tid]
                print("Транзакцію видалено.")
            else:
                print("Транзакцію не знайдено.")

        elif choice == "4":
            tid = input("ID для редагування: ")
            if tid not in financeTransactions:
                print("Транзакцію не знайдено.")
                continue

            old = financeTransactions[tid]

            try:
                amt = float(input("Нова сума: "))
                curr = input("Нова валюта: ").upper()
                cat = input("Нова категорія(Їжа/Транспорт/Розваги): ")

                if curr not in coursesBudgets.exchangeRates or cat not in coursesBudgets.categoryBudgets:
                    print("Невірні дані.")
                    continue

                budgetTrackers[old["category"]]["remove"](old["baseAmount"])
                base = convertToBase(amt, curr)

                if not budgetTrackers[cat]["add"](base):
                    budgetTrackers[old["category"]]["add"](old["baseAmount"])
                    continue

                financeTransactions[tid] = {
                    "amount": amt,
                    "currency": curr,
                    "baseAmount": base,
                    "category": cat
                }
                print("Транзакцію оновлено.")
            except ValueError:
                print("Помилка введення.")

        elif choice == "5":
            generateReport()

        elif choice == "6":
            break
