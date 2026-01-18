import streamlit as st

if 'all_accounts' not in st.session_state:
    st.session_state.all_accounts = []

all_accounts=[]
closed_account = []
import random
# function to open account
def open_account(cnic, title, initial_deposit):
    account = {'cnic'            :cnic,
               'title'           :title,
               'balance'         :initial_deposit,
               'account_number'  :random.randint(1001,9999),
               'pin'             :random.randint(1001,9999)
              }
    st.session_state.all_accounts.append(account)
    return account
# Function to show current balance
def check_balance(account, pin):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            if acc['pin']==pin:
                return acc['balance'], None
            else:
                return None, "Invalid Pin"
                
    else:
        return None, 'Invalid Account Number'
    
# function to withdraw amount
def withdraw(account, pin, amt):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            if acc['pin']==pin:
                if acc['balance']>=amt:
                    acc['balance']-=amt
                    return acc['balance'], None
                else:
                    return None, "Insuffiscent Balance"
            else:
                return None, "Invalid Pin"                
    else:        
        return None, "Invalid Account Number" 
# Function to deposit amount
def deposit(account,amt):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            acc['balance'] += amt
            return acc['balance'] , None 
    else:        
        return None, "Invalid Account Number" 
# Function to transfer amount
def transfer(account, pin ,amt, bacc):
    for ba in st.session_state.all_accounts:
        if ba['account_number']==bacc:        
            for acc in st.session_state.all_accounts:
                if acc['account_number']==account:
                    if acc['pin']==pin:
                        if acc['balance']>=amt:
                            ba['balance']+=amt
                            acc['balance']-=amt
                            return acc['balance'], None
                        else:
                            return None, "Insufficient Amount"
                    else:
                        return None, "Invalid Pin"                
            else:        
                return None, "Invalid Account Number" 
    else:
        return None, "Invalid Beneficiary Account Number"
# function to close account
def close_account(account, pin):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            if acc['pin']==pin:
                closed_account.append(st.session_state.all_accounts.pop(st.session_state.all_accounts.index(acc)))
                return acc , None
            else:
                return None, "Invalid Pin"
    else:
        return None,  "Invalid Account Number"
# Function to change PIN
def change_pin(account, pin, new_pin):
    for acc in st.session_state.all_accounts:
        if acc['account_number']==account:
            if acc['pin']==pin:
                acc['pin']=new_pin
                return acc['pin'], None
            else:
                return None, "Invalid Pin"
    else:
        return None, "Invalid Account Number"
#function to show all accounts
def show_all_accounts():
    return st.session_state.all_accounts

# Interface to user using streamlit
st.title("Simple Banking System")
st.write("This is a simple banking system built using Streamlit.")

menu = st.sidebar.selectbox(
    "Select Action",
    ["Open Account", "Check Balance", "Deposit", "Withdraw", "Transfer", "Show All Accounts", 'Close Account', "Change Pin"]
)

if menu == 'Open Account':
    st.header("Open a New Account")

    cnic = st.number_input('Enter Cnic')
    title = st.text_input('Account Title')
    deposi = st.number_input("Initial Deposit")

    if st.button("Create Account"):
        acc = open_account(cnic,title,deposi)
        st.success("Account Created Succesfully")
        st.write(f"**Account Number:** {acc['account_number']}")
        st.write(f"**pin:** {acc['pin']}  (save this!)")

if menu == 'Close Account':
    st.header("Close An Account")

    account = st.number_input("Enter Your Account Number")
    pin = st.number_input("Enter Pin")

    if st.button("Close Account"):
        acc, error = close_account(account,pin)
        if acc:
            st.success(f"""Your Account Has Been Closed Succesfully 
                       {acc}""")
        else:
            st.error(error)

if menu == 'Change Pin':
    st.header("Change Pin")

    account = st.number_input('Enter Your Account Number')
    pin = st.number_input("Enter A pin")
    new_pin = st.number_input("Enter Your New Pin")

    if st.button("Change"):
        acc, error = change_pin(account, pin, new_pin)
        if acc:
            st.success(f"{acc} (Save This New Pin!)")
        else:
            st.error(error)
    
if menu == "Check Balance":
    st.header('Check Balance')

    account = st.number_input("Enter Account Number")
    pin = st.number_input("Enter Your Pin")

    if st.button("Show Balance"):
        balance, error = check_balance(account, pin)
        if balance:
            st.success(f"Cureent Balance: {balance}")
        else:
            st.error(error)

if menu == "Deposit":
    st.header("Deposit")

    account = st.number_input("Enter Account Number")
    amt = st.number_input("Enter Amount")

    if st.button('Deposit'):
        balance, error = deposit(account,amt)
        if balance:
            st.success(f"{amt} Succesfully Deposited, Now Your Current Balance : {balance}")
        else:
            st.error(error)

if menu == "Withdraw":
    st.header('withdraw')

    account = st.number_input("Enter Account Number")
    pin = st.number_input("Enter Pin")
    amt = st.number_input('Withdraw Amount')

    if st.button("Withdraw"):
        balance, error = withdraw(account, pin, amt)
        if balance:
            st.success(f"{amt}Rs Succesfully Withdrawl, Your Current Balance Is : {balance}")
        else:
            st.error(error)

if menu == "Transfer":
    st.header("Transfer")

    account = st.number_input("Enter account Number")
    pin = st.number_input("Enter Pin")
    bacc = st.number_input("Enter Banificcially Account Number")
    amt = st.number_input("Enter Ammount")

    if st.button("Transfer"):
        balance, error = transfer(account, pin ,amt, bacc)

        if balance:
            st.success(f"{amt}Rs Succesfully Transfer, Your Remaining Balance Is : {balance}")
        else:
            st.error(error)

if menu == "Show All Accounts":
    st.header("Show All Accounts")

    if st.button("Show All Account"):
        acc = show_all_accounts()
        st.success(acc)