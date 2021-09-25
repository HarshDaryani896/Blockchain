# Importing the libraries
import requests
import subprocess
import os
import threading
import json
import pandas as pd

# setting output confiuration for pandas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

# Change this address according to the address in the flask server. 
node = "192.168.1.2:5001"

# This command will run our BC node in a separate cmd
os.system("start cmd /k python BC_node.py")

# The following commands will show the menu to choose from 
while(True):
    print("\n\nDexter Cafe Log on the Blockchain\n\n")
    print("A: Enter a transaction to the Blockchain")
    print("B: View all Blocks")
    print("C: View all Transactions in each block")
    print("D: Exit")
    option = input("Select your option:   ")

    if option =="A":
        print("\n\nOption A is selected")
        trx_name = input("Please enter name customer:  ")
        trx_amount = input("Please enter amount that he/she paid:  ")
        data_to_upload = {"sender":trx_name,"receiver":"Dexter","amount":trx_amount}

        # Adding the transaction data to transactions list
        response = requests.post(f'http://{node}/add_transaction', data= json.dumps(data_to_upload))
        mineRequest = requests.get(f'http://{node}/mine_block')
        print(f"\n\n {mineRequest.text}")


    elif option =="B":
        print("\n\nOption B is selected")

        # Get all the blocks from the Blockchain by using requests library
        response = requests.get(f'http://{node}/get_chain')
        print(response.text)
        
    elif option =="C":
        print("\n\nOption C is selected")

        # Get all the transactions from the existing blocks
        response = requests.get(f'http://{node}/get_chain')
        data_in_json = json.loads(response.text)
        required_data = data_in_json['chain']

        # Printing all transactions in tabular form
        df = pd.DataFrame(required_data)
        print(df)

    elif option =="D":

        # Exiting the loop
        print("\n\nExiting....")
        exit()

    else:
        print("\n\nInvalid option selected, please try again")


