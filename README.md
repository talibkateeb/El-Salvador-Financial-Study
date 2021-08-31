# El SALVADOR FINANCIAL STUDY
### A Machine Learning and Cryptocurrency Wallet Project
___
Under Construction

![672z311_1624612536_2021-06-25-10-15-36_bd8d86a1a8305bb40f40338ca257baad](https://user-images.githubusercontent.com/80144026/131263588-f9b3eb17-8d15-4811-a86d-4542a0b3d1ce.jpg)

<img width="1604" alt="Crypto_remittance_app_logo" src="https://user-images.githubusercontent.com/80144026/131263595-d1f1f044-d28f-4125-ace4-42eec48a73ac.png">

## Presentation with Results and Analysis

[Click here to view our full presentation with the results and analysis]

___

## Executive Summary
UNDER CONSTRUCTION

___

## Project Goals 
UNDER CONSTRUCTION

___

## Project Sections 

* MACHINE LEARNING ANALYSIS 
* CRYPTO CURRENCY REMITTANCE APP

___

## Machine Learning Models

* Supervised Learning: Logistic Regression
* Time Series: Facebook Prophet

___

## Data Collection Source

UNDER CONSTRUCTION
___

## Results and Analysis 

UNDER CONSTRUCTION

___

## Conclusion

___

## Next Steps

___

## Technologies

This project is written in Python within the Jupyter Lab environment  and VS Code with the following packages:

* Pandas
* Numpy
* Scikit Learn
* Hvplot
* FBProphet
* Streamlit
* Web 3
* Eth Tester
* mnemonic
* bip44
* Infura API https://infura.io

___

## Installation Guide
Before running the application first install and verify the following dependencies:

* Pandas from PyPI
```python
pip install pandas
```
* Numpy from PyPI
```python
pip install numpy
```
* Scikit Learn from PYPI
```python
pip install -U scikit-learn
```
* HVPLOT using Conda. Best practice, use an environment rather than install in the base env
 ```python
 conda activate dev 
 conda install -c pyviz hvplot 
```
* FBProphet using Conda. The easiest way to install is through Conda. Best practice, use an environment rather than install in the base env
 ```python
 conda activate dev 
 conda install -c conda-forge prophet
 ```
* Steamlit from PyPI
 ```python
 pip install streamlit
 ```
 
* Web 3 from PyPI
 ```python
 pip install web3==5.17
 ```
 * Eth Tester from PyPI
 ```python
 pip install eth-tester==0.5.0b3
 ```
 * Mnemonic from PyPI
 ```python
 pip install mnemonic
 ```
 * Bip 44 from PyPI
 ```python
 pip install bip44
 ```
 
Next, Import the Modules

ELSL_Financial_Study.ipynb:

```python
import pandas as pd
import numpy as np
from pathlib import Path
from pandas.tseries.offsets import DateOffset
from fbprophet import Prophet
import hvplot.pandas
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import warnings
warnings.filterwarnings('ignore')
 ```
 
Crypto_wallet.py:

 ```python
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3.auto.infura.kovan import w3
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
```
Crypto_Remittance_App.py:

 ```python
 import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from PIL import Image
`````

Clone to your local repo and run the following files:

* ELSL_Financial_Study.ipynb on Jupyter lab
* Crypto_wallet.py on Vs Code
* Crypto_Remittance_App.py on VS Code

___

### How to install, navigate and inspect transactions for Crypto Remittance App:

1. From your terminal, navigate to the project folder that contains
your `.env` file and the `crypto_remittance_app.py` and `crypto_wallet.py` files.
Be sure to activate your Conda `dev` environment if it is not already active.

2. To launch the Streamlit application, type `streamlit run crypto_remittance_app.py`.

3. On the resulting webpage, select a friend or family that you would like to send 
your cryptocurrency to from the appropriate drop-down menu. Then, enter the amoutn in USD or native fiat 
currency where the friend or family lives.

4. Click the Send Transaction button to sign and send the transaction with
your Ethereum account information. If the transaction is successfully
communicated to the Ethereum Kovan testnet, validated, and added to a block,
a resulting transaction hash code will be written to the Streamlit
application sidebar.

5. Copy your friend or family's Ethereum address from the Streamlit application
page, and navigate to [Kovan Etherscan](https://kovan.etherscan.io/).
Paste your copied Ethereum address into the Kovan Etherscan search bar.

6. On the Kovan Etherscan page, click on the Txn Hash number associated with
the transaction that sent remittance to your friend or family to verify by clicking
transaction details


## Contributors

* [Talib Kateeb](https://github.com/talibkateeb)
* [Van Maquilan](https://github.com/VanMSM)

___

## License
