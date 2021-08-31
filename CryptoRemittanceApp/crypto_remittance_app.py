# Cryptocurrency Remittance App


# We are building a crypto remittance app that friends 
# and family members can use to send cryptocurrency anywhere in the world.
# It will send transaction to the Kovan testnet.

# You can do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total amount Ethereum transaction in US Dollars or the native
# fiat currency of your friend or family , including the gas
# estimate.

# * Digitally sign a transaction  and send this transaction to the Kovan testnet.

# * Review the transaction hash code associated with the validated blockchain transaction.

# Once you receive the transaction’s hash code, you will navigate to [Kovan’s
# Etherscan](https://kovan.etherscan.io/) website to review the blockchain
# transaction details.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from PIL import Image

################################################################################
# Step 1:
# Import Ethereum Transaction Functions into the Crypto Remittance Application
# Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`


# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
#Friend and Family Information

# Database of Friends including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $3,208.01
friend_database = {
    "Venice": ["Venice", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", " New York, US Dollar (USD)",0.0003,  "Images/Venice.png"],
    "Jane": ["Jane", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", " El Salvador, US Dollar (USD)",0.0003, "Images/Jane.png"],
    "Pia": ["Pia", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "Philippines, Philippine Peso (PHP)", 0.000006, "Images/Pia.png"],
    "Chris": ["Chris", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "California, US Dollar (USD)",0.0003, "Images/Chris.png"]
}

# A list of the friends and family's first names
people = ["Venice", "Jane", "Pia", "Chris"]


def get_people():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(friend_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("Location:", db_list[number][2])
        st.write("currency conversation rate: ", db_list[number][3], "eth")
        st.text(" \n")
       

 
        

################################################################################
# Streamlit Code

# Streamlit application headings
img = Image.open("Images/Crypto_remittance_app_logo.png")

st.image(img)
st.markdown("# Send cryptocurrency to friends and family anywhere in the world!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Friend Account Address and Ethernet Balance in Ether")

##########################################

# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Fintech Finder
# customer’s (in this case, your) HD wallet and Ethereum account.


#  Call the `generate_account` function and save it as the variable `account`

account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################

# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar

st.sidebar.write(get_balance(account.address))

##########################################

# Create a select box to chose a friend
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the amount in USD or other currency
Amount_to_send = st.sidebar.number_input("Remittance Amount in Native Fiat Currency")

st.sidebar.markdown("## Friend Name, Remittance Amount, and Ethereum Address")

# Identify the Friend or Family
friend = friend_database[person][0]

# Write the Friend or Family name to the sidebar
st.sidebar.write(friend)

# Identify the Friend or Family Fiat Currency
selected_currency = friend_database[person][3]

# Write the Friend or Family's fiat currency
st.sidebar.write(selected_currency)

# Identify the Friend or Family's Ethereum Address
friend_address = friend_database[person][1]

# Write the Friend or Family's Ethereum Address to the sidebar
st.sidebar.write(friend_address)

# Write the Friend or Family's name to the sidebar

st.sidebar.markdown("## Total Amount in Ether")

################################################################################
# Step 2: Sign and Execute a Payment Transaction


# * Write the equation that calculates the amount in USD vs amount in Ethereum
# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
total_remittance = friend_database[person][3]* Amount_to_send


# Write the "total_remittance" calculation to the Streamlit sidebar

st.sidebar.write(total_remittance)

##########################################


# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.


if st.sidebar.button("Send Transaction"):

   
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(account, friend_address,Amount_to_send)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes Crypto Remittance App to the Streamlit page
get_people()

################################################################################
#How to Inspect the Transaction on Etherscan

# Send a test transaction by using the application’s web interface, and then
# look up the resulting transaction hash on the Kovan Etherscan block explorer
# to verify the transactions.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `crypto_remittance_app.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# 2. To launch the Streamlit application,
# type `crypto_remittance_app.py`.

# 3. On the resulting webpage, select a friend or family that you would like to send 
#your cryptocurrency to from the appropriate drop-down menu. Then, enter the amoutn in USD or native fiat 
# currency where the friend or family lives.

# 4. Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to the Ethereum Kovan testnet, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

# 5. Copy your friend or family's Ethereum address from the Streamlit application
# page, and navigate to [Kovan Etherscan](https://kovan.etherscan.io/).
# Paste your copied Ethereum address into the Kovan Etherscan search bar.

# 6. On the Kovan Etherscan page, click on the Txn Hash number associated with
# the transaction that sent remittance to your friend or family to verify by clicking
# transaction details

    
