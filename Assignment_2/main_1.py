#main_1.py

import requests


import subprocess
import os
import threading
import json
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


# Change this address according to the address in the flask server. 
port = "5001"
node = f"192.168.1.6:5001/"


# This command will run our BC node in a separate cmd
for i in range(1,4):
    os.system(f"start cmd /k python BC_node_{i}.py")

### Part 2A -- Connecting the nodes
# To connect all the nodes
nodes_data = json.load(open('nodes.json','r'))
node_connect_response = requests.post(f'http://{node}/connect_node', data= json.dumps(nodes_data))


# The following commands will show the menu to choose from 
while(True):
    print("Dexter Cafe Log on the Blockchain\n\n")

    print("a: Enter a transaction to the Blockchain")
    print("b: View all Blocks")
    print("c: View all Transactions in each block")
    print("d: Select the Miner node (if the selected node is not validator, the transaction will not be mined.)")
    print("e: Show the current miner node")
    print("f: Exit")
    option = input("Select your option:   ")


    if option =="a":
        print("\n\nOption A is selected")
        trx_name = input("Please enter name customer:  ")
        trx_amount = input("Please enter amount that he/she paid:  ")

        data_to_upload = {"sender":trx_name,"receiver":"Dexter","amount":trx_amount}
        # data_to_upload = json(data_to_upload)

        response = requests.post(f'http://{node}/add_transaction', data= json.dumps(data_to_upload))

        mineRequest = requests.get(f'http://{node}/mine_block')

        print(f"\n\n {mineRequest.text}")


    elif option =="b":
        print("\n\nOption B is selected")
        # Get all the blocks from the Blockchain by using requests library
        response = requests.get(f'http://{node}/get_chain')
        print(response.text)
        
    elif option =="c":
        print("\n\nOption C is selected")
        # Get all the transactions from the existing blocks
        nodes_data = json.load(open('nodes.json','r'))
        node_connect_response = requests.post(f'http://{node}/connect_node', data= json.dumps(nodes_data))
        resp_1 = requests.get(f'http://{node}/replace_chain')
        response = requests.get(f'http://{node}/get_chain')
        
        data_in_json = json.loads(response.text)
        required_data = data_in_json['chain']
        for i in range(len(required_data)):
            print(required_data[i])
        # df = pd.DataFrame(required_data)
        # print(df)


    elif option== "d":
        print("Option C is selection")
        while(True):
            miner_option = input("Please select your miner:  (\n1 for validator  \n2 for normal BC nodes \n3 for normal BC nodes \n4 to return to main menu \n\n)")
            
            if miner_option=="1":
                port = "5001"
                node = f"192.168.1.24:{port}"
                break

            elif miner_option=="2":
                port = "5002"
                node = f"192.168.1.24:{port}"
                break

            elif miner_option=="3":
                port = "5003"
                node = f"192.168.1.24:{port}"
                break

            elif miner_option=="4":
                break
            else:
                print("invalid option is selected")
                

            
    elif option == "e":
        print(f"\n\n The current selected miner node is-->  {node}\n\n")

    elif option =="f":
        print("\n\nExiting....")
        exit()
    else:
        print("\n\nInvalid option selected, please try again")


