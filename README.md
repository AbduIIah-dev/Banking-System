# Banking-System
A simple banking system built with Python and Streamlit.
Manage accounts, check balances, deposit, withdraw, transfer funds, change PINs, and close accounts with an easy-to-use interface.

## Features
- Open a new account with CNIC, title, and initial deposit
- Check account balance securely using PIN
- Deposit money into accounts
- Withdraw money from accounts
- Transfer money between accounts
- Change account PIN
- Close an account
- Show all accounts (for testing purposes)

## Installation
1. Clone this repository:
   git clone https://github.com/Abdullah-dev/Simple-Banking-System.git
2. Navigate to the project directory:
   cd Simple-Banking-System
3. Install the required packages:
   pip install streamlit

## Usage
Run the Streamlit app using:
streamlit run app.py

Use the sidebar to select actions like "Open Account", "Deposit", "Withdraw", etc.
Follow on-screen instructions to manage your accounts.

## Notes
- Account numbers and PINs are generated randomly.
- This is a simple educational project, not for real banking use.
- Data is stored only in the session state; closing the app will reset all accounts.

## License
This project is licensed under the MIT License.

