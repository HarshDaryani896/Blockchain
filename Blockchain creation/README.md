# Dexter's Blockchain

Blockchain Programming Assignment 1

## Group Details

Group Number - G34	
- 2018B3A70992H	Rohan Sachan
- 2018B1A70645H	Harsh Daryani
- 2018A7PS0176H	Kanishk Pathak

## How to run?

    • Create a python virtual environment.
    • It is advised that the libraries mentioned in the requirements.txt should be installed before running this code. “pip install -r requirements.txt”.
    • Change the address on Line 16 of main_1.py according to the address of flask server for your system.
    • After installing all the libraries, run the main_1.py
    • This will run a flask server (BC_node.py). You can minimize that and focus on the main_1.py window.
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
