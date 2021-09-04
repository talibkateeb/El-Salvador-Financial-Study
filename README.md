# El SALVADOR'S ROAD TO CRYPTOCURRENCY, AN ECONOMIC ANALYSIS
### A Machine Learning and Cryptocurrency Wallet Project
___

![672z311_1624612536_2021-06-25-10-15-36_bd8d86a1a8305bb40f40338ca257baad](https://user-images.githubusercontent.com/80144026/131263588-f9b3eb17-8d15-4811-a86d-4542a0b3d1ce.jpg)

## Presentation with Results and Analysis

[Click here to view our full presentation with the results, analysis, and graphs!](https://prezi.com/view/EQjzqC6LXpAA5Wk5q0t5/)
___

## Executive Summary

In this project,  we are conducting an analysis on El Salvador’s Road to Cryptocurrency.

El Salvador is a country in Central America with about 6.5 million people. Their president is Nayib Bukele.

In 2001, El Salvador adopted the Dollarization, which allowed the  US dollar to circulate at par with the local currency, the colón. 

On September 7, 2021, El Salvador will be the first nation in the world to adopt Bitcoin as a legal tender.

We chose  to study El Salvador because we’re very interested in how the Dollarization impacted its economy and what the Bitcoin adoption will bring to the country moving forward.

___

## Project Sections

PART ONE: 

We analyzed and forecasted the economic state of the nation of El Salvador. We examined different measurements such as GDP, GNI, Gini Index, etc. and created models to forecast these measurements to see how the adoption of Bitcoin as a legal tender will affect the nation.

PART TWO: 

We surveyed the remittance market in El Salvador, identified a problem and created a possible solution: A crypto remittance application to lower the  cost for the remittance senders and increase the remittance income of the people of El Salvador, increase beneficiary spending which will positively impact the country's economy.

___

## Data Collection Source

* The World Bank

* Statista

* Trading Economics

___

## PART ONE: Data Analysis and Forecasting

### Economic Data

 ##### GROSS DOMESTIC PRODUCT

<img width="541" alt="Screen Shot 2021-09-02 at 11 19 02 PM" src="https://user-images.githubusercontent.com/80144026/131959519-d01d7b33-4bc4-4206-8104-5aa187d47fc2.png">

 ##### POPULATION

<img width="519" alt="Screen Shot 2021-09-02 at 11 19 53 PM" src="https://user-images.githubusercontent.com/80144026/131959570-4659f05a-4917-43a1-8b24-5268e20b7596.png">

 ##### GROSS NATIONAL INCOME

<img width="537" alt="Screen Shot 2021-09-02 at 11 20 27 PM" src="https://user-images.githubusercontent.com/80144026/131959660-fbdb58cf-c3fe-4b88-a2d8-47d52f255e3c.png">

 ##### GINI INDEX

<img width="530" alt="Screen Shot 2021-09-02 at 11 21 26 PM" src="https://user-images.githubusercontent.com/80144026/131959738-4efa18cd-7398-4b63-8739-afd50467b08c.png">

 ##### INFLATION RATE

<img width="526" alt="Screen Shot 2021-09-02 at 11 52 37 PM" src="https://user-images.githubusercontent.com/80144026/131963193-de8e2c0a-1a7c-4140-8689-268c415a8f05.png">



---

## Forecasting

### Machine Learning/Time Series Models Used

- Prophet
- Theta
- Linear Regression
- Fast Fourier Transform

#### DARTS
 
  ###### METRICS
 <img width="408" alt="Screen Shot 2021-09-02 at 11 23 15 PM" src="https://user-images.githubusercontent.com/80144026/131959907-7e4fea45-ff2b-47ea-8b45-7478679b1787.png">
 <img width="432" alt="Screen Shot 2021-09-02 at 11 23 20 PM" src="https://user-images.githubusercontent.com/80144026/131959911-2e1eefa2-efd1-45f0-92ee-78573f2345e5.png">
 
### Forecast Results Visualization
  
  ###### GINI INDEX

 <img width="328" alt="Screen Shot 2021-09-02 at 11 25 39 PM" src="https://user-images.githubusercontent.com/80144026/131960151-65e64a9b-ee3c-4c9c-8adf-88e1f25cef2b.png">
 
  ###### GDP
  
<img width="326" alt="Screen Shot 2021-09-02 at 11 25 48 PM" src="https://user-images.githubusercontent.com/80144026/131960160-a954cda3-2034-438e-a60e-4c6a378e52ff.png">



#### FACEBOOK PROPHET

 ###### GDP

 
<img width="552" alt="Screen Shot 2021-09-02 at 11 49 03 PM" src="https://user-images.githubusercontent.com/80144026/131962747-f2540460-4e93-4f79-b052-4b8b4d6dcce2.png">


 ###### GNI

<img width="544" alt="Screen Shot 2021-09-02 at 11 30 21 PM" src="https://user-images.githubusercontent.com/80144026/131960939-9c295655-341b-4ff4-981b-145c521e4ac5.png">


 ###### GINI INDEX

<img width="561" alt="Screen Shot 2021-09-02 at 11 52 19 PM" src="https://user-images.githubusercontent.com/80144026/131963216-ab0c00ef-cfbb-4308-aba1-2244f56785ea.png">


###### INFLATION RATE

<img width="553" alt="Screen Shot 2021-09-02 at 11 34 49 PM" src="https://user-images.githubusercontent.com/80144026/131961064-d03345ad-1a4b-4358-88e4-432b793ae630.png">


___

### Analysis 

- The inflation dataset had extremely high values for MAPE and almost zero values for MSE across all models, indicating overfitting. 

- Gross National Income Dataset had extremely high values for MSE indicating very high variance/bias

- Gini Index dataset: Prophet model performed the best, we use that to perfrom the forecast, it performed better on training set split before 2010

- GDP: Linear Regression performs the best on training set split before 2005

- The data shows that the Dollarization had a positive impact on El Salvador's economy.

- Forecast results show that the economy of El Salvador will be on a positive trajectory in the next 10 years.

___

## PART TWO: Remiitance


 ### El Salvador is a country whose economy relies heavily on international remittance,  a lifeline for millions.
 
<img width="1052" alt="Screen Shot 2021-08-31 at 2 19 26 PM" src="https://user-images.githubusercontent.com/80144026/131958446-543686d8-f96f-4833-92be-33ed449884bf.png">

### STATISTICS

* Total average monthly remittance received for the whole country  is $623.18 million dollars, that’s about 7.4 Billion dollars a year! And the  total cost to send is $186.954 to $224 million dollars a year.
* Almost 1 of 5 of every Salvadorans receive remittances from abroad, 70% are women.
* Majority of the remittance benificiaries live in San Salvador.
* Of all the recipients, 43% are the vulnerable , 32.6% are poor, 28% have no formal education, 21% have no access to running water, 5% have no access to bathroom facilities and 7% have no access to electricity
* Remittance Use: 94% daily consumption expenditures, 10% for education, 5% use it for healthcare, the rest are for savings and other uses.
* The mean remittance income is $195 US dollars.
* Personal Remittances have steadily gone up since 1976, and in 2020 it was almost 25% of the country’s Gross Domestic Product.

<img width="694" alt="Screen Shot 2021-08-31 at 8 03 10 PM" src="https://user-images.githubusercontent.com/80144026/131958044-bb2b6f42-4f8f-48d7-bead-97e9ee8c887b.png">


* The average cost of sending remittances in El Salvador is between 2.5- 3.0% of the amount sent.

<img width="749" alt="Screen Shot 2021-08-31 at 8 02 46 PM" src="https://user-images.githubusercontent.com/80144026/131958059-364ab329-25e2-4952-a194-72adc1c5c36d.png">

* The average monthly remittance for the entire country: $623.18 Million.

<img width="1088" alt="Screen Shot 2021-09-02 at 11 37 36 PM" src="https://user-images.githubusercontent.com/80144026/131961414-c21ad749-581d-4e59-92af-895c14d846f3.png">

### With this information, we asked ourselves:


*What if we can reduce the fees for the senders so they can send more money to the beneficiaries? More money for food, education, basic services and healthcare?*

___

#### To solve this problem, we created THE CRYPTO REMITTANCE APP, a solution that can help lower remittance fees, and increase personal remittance income for the benefiaciaries. This application will allow friends and family to send cryptocurrency wherever they are in the world and it has a simple built in  fiat to cryptocurrency conversion function.

<img width="1272" alt="Screen Shot 2021-08-31 at 2 50 22 PM" src="https://user-images.githubusercontent.com/80144026/131958160-8d6fc0b4-da18-481c-b1aa-350c03ed7412.png">


### Watch how it works:


https://user-images.githubusercontent.com/80144026/131958640-b6d8806a-1232-40d6-a5ef-43166846c29e.mov


___


## Conclusion

* Based on our Analysis, the Dollarization impacted the economy of El Salvador positively.

* El Salvador Bitcoin Law will be implemented on  September 7, 2021. Based on the forecast we trust the most, the income inequality in El Salvador should be decreasing. Will the adoption of Bitcoin as a legal tender deter or speed up that outcome? We will find out in a few years.

___

## Next Steps

* For the Crypto Remittance App, we want to add functionalities like pull info from social media accounts and from smart phone contacts, and add a real time fiat to cryptocurrency conversion.

* Acquire more data for forecasting.

* Hyperparameter optimization for models evaluated.

* Revisit our analysis in a few years.
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
* Darts

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
* Darts from PYPI
```python
pip install darts
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

[Click here to view MIT License](https://github.com/talibkateeb/El-Salvador-Financial-Study/blob/main/LICENSE)


