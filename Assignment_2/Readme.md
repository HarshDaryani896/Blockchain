In this project, I have added proof of authority as a consensus algorithm and extended the main menu to add few more elements.

Tutorial:

-	Please follow the same steps as earlier. Like create the virtual environment, activate it, and  install the requirements.
-	Run the main_1.py
-	Please update the IP addresses in each file according to your need. Because the IP addresses may change on the system that it is run on.
-	When this program is run, it will spawn 3 additional terminals. Each of these terminals represent a Blockchain node.
-	Among these nodes, the one running on port 5001 is a validator node. Means, this node can perform mining, while other nodes cannot.
o	I have added a list of validators in validators.txt. Here we can add the node_ID of the BC_nodes. The node_ID is available in each BC_node file.
-	The main menu has been extended. I have added a menu item which can be used to select different BC_nodes to see if their local BC ledger has been updated.
o	Also, when a non-validator node is selected, the transactions will not be added to the BC ledger. 
o	This will help us better understand how the BC works when PoA consensus is used.
-	The local BC ledger of each node will be updated when a new transaction is mined. This will show that this system is truly decentralized. 
-	New nodes can be added by creating a copy of the BC_node_{increment the number}, and also add the port number to nodes.json
-	The code is also commented to know where the changes are made.
