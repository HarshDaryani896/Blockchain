# Dexter’s Consensus Algorithm

Blockchain Programming Assignment 2

## Group Details

Group Number - G34	
- 2018B3A70992H	Rohan Sachan
- 2018B1A70645H	Harsh Daryani
- 2018A7PS0176H	Kanishk Pathak

## How to run?

    • Create a python virtual environment.
    • It is advised that the libraries mentioned in the requirements.txt should be installed before running this code. “pip install -r requirements.txt”.
    • Change the address on Line 16 of main_1.py and in BC_Node files according to the address of flask server for your system.
    • After installing all the libraries, run the main_1.py
    • This will run flask servers for each node. You can minimize that and focus on the main_1.py window.
    • Select the desired option to run it following the direction of menu.
    • After closing, make sure you also close the flask server cmd in the background.
    
## Special Libraries used
For this project we have used the following libraries:

1. Flask:
We have used this library to create our Blockchain nodes. By using Flask, we were able to create our Blockchain as a server using flask.
2. hashlib:
We used this library to create hashes of my blocks. I also used it for the mining process. In mining process, I created a simple Proof of Work module.
3. requests:
We used this library in my main file and the Blockchain node as well. This library enables sending get and post requests
4. json:
We used this library to convert my python dictionary into json before sending in the post request. Also, the data retrieved from the Blockchain is converted back into json for better viewing.

## Updates in Assignment 2
In this assignment, we have added Proof of Authority (PoA) as a consensus algorithm and extended the main menu to add few more elements.

-	When this program is run, it will spawn 3 additional terminals. Each of these terminals represent a Blockchain node.
-	Among these nodes, the one running on port 5001 is a validator node. Means, this node can perform mining, while other nodes cannot.
-	We have added a list of validators in validators.txt. Here we can add the node_ID of the BC_nodes. The node_ID is available in each BC_node file.
-	The main menu has been extended. We have added a menu item which can be used to select different BC_nodes to see if their local BC ledger has been updated.
-	Also, when a non-validator node is selected, the transactions will not be added to the BC ledger. This will help us better understand how the BC works when PoA consensus is used.
-	The local BC ledger of each node will be updated when a new transaction is mined. This will show that this system is truly decentralized. 
-	New nodes can be added by creating a copy of the BC_node_{increment the number}, and also add the port number to nodes.json
-	The code is also commented to know where the changes are made.
