class ExpenseManager:
    def __init__(self):
        self._expenses = []

    def add_expense(self, amount, category, description=""):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if not category.strip():
            raise ValueError("Category cannot be empty")

        expense = {
            "amount": round(float(amount), 2),
            "category": category.strip(),
            "description": description.strip()
        }
        self._expenses.append(expense)
        return expense

    def get_total(self):
        return round(sum(item["amount"] for item in self._expenses), 2)

    def get_expenses_by_category(self, category):
        return [
            item for item in self._expenses
            if item["category"].lower() == category.lower()
        ]

    def get_expenses(self):
        return list(self._expenses)


def main():
    manager = ExpenseManager()
    print("=== Expense Tracker ===")
    while True:
        print("\n1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                description = input("Description: ")
                manager.add_expense(amount, category, description)
                print("Expense added successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            expenses = manager.get_expenses()
            if not expenses:
                print("No expenses recorded.")
            else:
                for item in expenses:
                    print(
                        f'{item["category"]}: '
                        f'{item["amount"]:.2f} - {item["description"]}'
                    )

        elif choice == "3":
            print(f"Total expenses: {manager.get_total():.2f}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
