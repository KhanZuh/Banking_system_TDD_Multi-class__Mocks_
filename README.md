# 🗄️ Project overview

As a bank customer, I want to:

1. Create an account with an initial balance
2. Deposit money into my account
3. Withdraw money (only if sufficient funds and transaction is valid)
4. Check my current balance
5. Have all transactions validated against fraud detection

### Technical Requirements:

- All transactions must be validated via external API
- Insufficient funds should raise appropriate errors
- Invalid transactions (flagged by API) should be rejected
- All classes should be thoroughly tested with mocks


### 🔧 Key Concepts You'll Practice

- Mocking external APIs - Don't make real HTTP calls in tests!
- Dependency injection - How to make classes testable
- Error handling - What happens when things go wrong?
- Integration testing - How do all the pieces work together?


 

## 📁 Project Structure

```
banking_system/
├── lib/
│   ├── account.py
│   ├── transaction_validator.py
│   └── banking_service.py
├── tests/
│   ├── test_account.py
│   ├── test_transaction_validator.py
│   └── test_banking_service.py
├── requirements.txt
└── README.md
```
### 🛠️ Local Environment Setup
```
mkdir banking_system
cd banking_system
```
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### requirements.txt
```
pytest==7.4.3
requests==2.31.0
pytest-mock==3.12.0
```
### Install dependencies
```
pip install -r requirements.txt
```

## Some notes to help you get started 

### Phase 1: Basic Account (Start Here)

- Make the failing test pass by creating Account class
- Add tests and implementation for deposit/withdraw operations
- Handle insufficient funds with proper exceptions

### Phase 2: Transaction Validator (The Tricky Part)

- Create TransactionValidator that calls external API
- Mock the API calls in your tests
- Handle API failures gracefully

### Phase 3: Banking Service (Integration)

- Create BankingService that uses both Account and TransactionValidator
- Test the full integration with mocks
- Debug any issues that arise

