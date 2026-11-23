import unittest

from expense_tracker import (
    add_expense,
    get_total,
    get_expenses_by_category,
    expenses
)


class ExpenseTrackerTests(unittest.TestCase):
    def setUp(self):
        expenses.clear()

    def test_add_expense(self):
        result = add_expense(25.50, "Food", "Lunch")
        self.assertEqual(result["amount"], 25.50)
        self.assertEqual(result["category"], "Food")

    def test_get_total(self):
        add_expense(10, "Food")
        add_expense(15.5, "Transport")
        self.assertEqual(get_total(), 25.5)

    def test_filter_by_category(self):
        add_expense(10, "Food")
        add_expense(20, "Transport")
        self.assertEqual(len(get_expenses_by_category("food")), 1)

    def test_reject_non_positive_amount(self):
        with self.assertRaises(ValueError):
            add_expense(0, "Food")

    def test_reject_empty_category(self):
        with self.assertRaises(ValueError):
            add_expense(10, "  ")


if __name__ == "__main__":
    unittest.main()
