import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        """Set up a test account before each test."""
        self.account = Account(acno=12345, customer_name="John Doe", balance=1000)

    def test_initialization(self):
        """Test account initialization."""
        self.assertEqual(self.account.acno, 12345)
        self.assertEqual(self.account.customer, "John Doe")
        self.assertEqual(self.account.balance, 1000)

    def test_deposit_valid_amount(self):
        """Test depositing a valid amount."""
        self.assertTrue(self.account.deposit(500))
        self.assertEqual(self.account.get_balance(), 1500)

    def test_deposit_invalid_amount(self):
        """Test depositing an invalid amount."""
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_valid_amount(self):
        """Test withdrawing a valid amount."""
        self.assertTrue(self.account.withdraw(500))
        self.assertEqual(self.account.get_balance(), 500)

    def test_withdraw_invalid_amount(self):
        """Test withdrawing an invalid amount."""
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    def test_withdraw_insufficient_balance(self):
        """Test withdrawing more than the balance."""
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_get_balance(self):
        """Test getting the current balance."""
        self.assertEqual(self.account.get_balance(), 1000)

    def test_str_representation(self):
        """Test the string representation of the account."""
        self.assertEqual(
            str(self.account),
            "Account Number: 12345, Customer Name: John Doe, Balance: 1000"
        )

if __name__ == "__main__":
    unittest.main()