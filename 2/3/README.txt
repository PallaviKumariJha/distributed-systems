Assignment: Chord Protocol Simulator
By: Pallavi Kumari Jha
	AM.EN.P2CSN16014

run the code: python chord.py

Steps:
1) User will be asked for number of Nodes to be inserted in chord ring
2) User inputs that many nodes in the chord ring and the corresponding finger table is generated.
3) User can delete any node. Finger table will change accordingly.
4) User can add any pre-existing node. Finger table will be changed accordingly.
5) User can find any file ID
	- user gives the file ID.
	- user gives the node to start the search from. 
	- node that containes that file ID will be printed.
	- complete path followed for that File ID from the start node will be printed as well.
6) User can add a key
	- user needs to give the key value,
	if key is not already present 
		- it will be added
	else
		- user will be promted that key is already existing with a particular node


Extra:
# If one does not want to give the nodes every time code is run
# For quick testing uncomment the following
# masterNodes = {16:[],32:[],45:[],80:[],96:[],112:[]}
# Comment out addMasterNodes() on line 59
# Uncomment createFingerTable(masterNodes) on line 189
# run the code