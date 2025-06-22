import pytest
from lib.account import Account

def test_account_requires_initial_deposit():
    with pytest.raises(ValueError, match="Account balance cannot be zero"):
        account = Account(0)

def test_account_initializes_with_balance():
    account = Account(100)
    assert account.balance == 100