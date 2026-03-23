from logic import *
from storage import *
from export import *

expenses = load_data()

while True:
    print("\n1. Pievienot izdevumu")
    print("2. Parādīt visus")
    print("3. Dzēst")
    print("4. Filtrēt pēc mēneša (YYYY-MM)")
    print("5. Kopsavilkums")
    print("6. Eksportēt CSV")
    print("0. Iziet")

    choice = input("Izvēle: ")

    if choice == "1":
        date = input("Datums (YYYY-MM-DD): ")
        amount = input("Summa: ")
        category = input("Kategorija: ")
        description = input("Apraksts: ")
        add_expense(date, amount, category, description)

    elif choice == "2":
        for i, e in enumerate(get_expenses()):
            print(i, e)

    elif choice == "3":
        index = int(input("Index: "))
        delete_expense(index)

    elif choice == "4":
        month = input("Mēnesis (YYYY-MM): ")
        for e in filter_by_month(month):
            print(e)

    elif choice == "5":
        total, categories = get_summary()
        print("Kopā:", total)
        print("Pa kategorijām:", categories)

    elif choice == "6":
        export_to_csv(get_expenses())

    elif choice == "0":
        save_data(get_expenses())
        break
    print("Programma darbojas")
    