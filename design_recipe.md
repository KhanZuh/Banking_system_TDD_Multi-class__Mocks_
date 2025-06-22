# Design recipe

"What does a banking system actually do in the real world?"
- Banks have accounts with balances
- People deposit and withdraw money
- Banks validate transactions for fraud
- Multiple systems work together

## User stories
```
As a bank customer, I want to:
- Create a new account with an initial deposit
- Check my current account balance  
- Deposit money into my account
- Withdraw money from my account (only if I have enough)
- Have my transactions checked for fraud automatically
- See a history of my transactions

As a bank system, I need to:
- Validate every transaction before processing
- Reject suspicious transactions
- Handle validation service outages gracefully
- Keep accurate records of all operations
- Prevent overdrafts
```

##  Identify Nouns and Verbs

### Nouns (potential classes):
- Account - stores balance, transaction history
- Transaction - represents money movement
- Validator - checks transaction legitimacy
- BankingService - orchestrates operations
- Balance - current money amount
- History - list of past transactions

### Verbs (Potential methods):
- create account
- deposit money
- withdraw money
- validate transaction
- check balance
- record transaction
- approve/reject transaction

### Initial class mapping:
```
Account:
  - deposit()
  - withdraw() 
  - get_balance()
  - get_history()

TransactionValidator:
  - validate_transaction()
  
BankingService:
  - process_deposit()
  - process_withdrawal()

```

## What if questions
What if there's insufficient funds?
- Decision: Raise `InsufficientFundsError`
- Reasoning: Clear, specific error that calling code can handle appropriately

What if the validation API is down?
- Decision: Raise `ValidationError`
- Reasoning: Don't fail silently; let system decide how to handle (retry, queue, etc.)

What if validation rejects the transaction?
- Decision: Raise `InvalidTransactionError`
- Reasoning: Different from API being down; this is a business rule rejection

What if negative amounts are passed?
- Decision: Raise `ValueError` in Account methods
- Reasoning: This is invalid input, not a business rule violation

What if account balance becomes negative due to a bug?
- Decision: Prevent in `withdraw()` method, don't allow negative balances
- Reasoning: Data integrity protection

What if we need transaction history?
- Decision: Account tracks all operations internally
- Reasoning: Simple audit trail, easy to implement and test


## Writing out the tests

### Identify Core Responsibilities
```
Banking System needs to:
├── Store account data (balance, history) → Account class
├── Validate transactions externally → TransactionValidator class  
└── Coordinate operations → BankingService class
```

- Account: Pure data + basic operations (no external dependencies)
- TransactionValidator: Handles ONE thing - external API calls
- BankingService: Orchestrates the workflow





## Account Class

The `Account` class manages individual bank account operations.

### Usage Examples

```python
# Initialize account with starting balance
account = Account(100)
account.balance  # => 100

# Deposit money
account.deposit(50)
account.balance  # => 150

# Withdraw money (sufficient funds)
account.withdraw(30)
account.balance  # => 120

# Withdraw money (insufficient funds) - should raise error
account = Account(20)
account.withdraw(50)  # => raises InsufficientFundsError("Cannot withdraw 50, balance is 20")

# Account history tracking
account = Account(100)
account.deposit(50)
account.withdraw(25)
account.transaction_history  # => [('deposit', 50), ('withdraw', 25)]
```

## TransactionValidator Class

When trying to figure out how to implement this class - i thought of simple examples.

TransactionValidator = Bouncer at a club

```
# How would you interact with a bouncer?
bouncer.check_id(person)  # Simple, clear
# → validator.validate_transaction(account_id, amount, type)

# What responses make sense?
bouncer_says = "You're good to go" or "Not happening"  
# → {"valid": True} or {"valid": False, "reason": "..."}
```

### Step 1: What does it actually do?
"Checks if a transaction is safe before allowing it"
### Step 2: What's the simplest input?
"I want to withdraw $50 from account 123"

```python
validator.validate_transaction("123", 50, "withdraw")
```

### Step3: Usage examples 
```python
validator = TransactionValidator()

# Happy path
result = validator.validate_transaction("ACC123", 100, "withdraw")
# result = {"valid": True, "message": "Transaction approved"}

# Rejection  
result = validator.validate_transaction("ACC123", 10000, "withdraw") 
# result = {"valid": False, "message": "Amount too large"}

# System error
validator.validate_transaction("ACC123", 100, "withdraw")
# raises ValidationError("Unable to connect to fraud detection service")
```

## BankingService Class

### Step 1: What's its job?
"Make withdrawals and deposits work smoothly by handling all the complexity"

### Step 2: What complexity is it hiding?
- Checking account balance
- Validating with external service
- Actually updating the account
- Handling when things go wrong

```Python
account = Account(1000)
validator = TransactionValidator()
service = BankingService(account, validator)

# Simple interface, complex work behind the scenes
service.withdraw(200)  # Validates, then withdraws
service.deposit(100)   # Validates, then deposits

# Clear errors
service.withdraw(2000)  # raises InvalidTransactionError("Flagged as suspicious")
service.withdraw(5000)  # raises InsufficientFundsError("Not enough funds")
```


