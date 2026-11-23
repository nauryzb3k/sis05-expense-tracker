import unittest

from expense_tracker import ExpenseManager


class ExpenseTrackerTests(unittest.TestCase):
    def setUp(self):
        self.manager = ExpenseManager()

    def test_add_expense(self):
        result = self.manager.add_expense(25.50, "Food", "Lunch")
        self.assertEqual(result["amount"], 25.50)
        self.assertEqual(result["category"], "Food")

    def test_get_total(self):
        self.manager.add_expense(10, "Food")
        self.manager.add_expense(15.5, "Transport")
        self.assertEqual(self.manager.get_total(), 25.5)

    def test_filter_by_category(self):
        self.manager.add_expense(10, "Food")
        self.manager.add_expense(20, "Transport")
        self.assertEqual(len(self.manager.get_expenses_by_category("food")), 1)

    def test_filter_by_category_matches_multiple(self):
        self.manager.add_expense(10, "Food")
        self.manager.add_expense(20, "food")
        self.assertEqual(len(self.manager.get_expenses_by_category("Food")), 2)

    def test_reject_non_positive_amount(self):
        with self.assertRaises(ValueError):
            self.manager.add_expense(0, "Food")

    def test_reject_negative_amount(self):
        with self.assertRaises(ValueError):
            self.manager.add_expense(-5, "Food")

    def test_reject_empty_category(self):
        with self.assertRaises(ValueError):
            self.manager.add_expense(10, "  ")

    def test_managers_do_not_share_expenses(self):
        manager_a = ExpenseManager()
        manager_b = ExpenseManager()

        manager_a.add_expense(10, "Food")

        self.assertEqual(len(manager_a.get_expenses()), 1)
        self.assertEqual(manager_b.get_expenses(), [])
        self.assertEqual(manager_b.get_total(), 0)

    def test_mutating_returned_list_does_not_affect_manager(self):
        self.manager.add_expense(10, "Food")

        expenses = self.manager.get_expenses()
        expenses.clear()

        self.assertEqual(len(self.manager.get_expenses()), 1)


if __name__ == "__main__":
    unittest.main()
