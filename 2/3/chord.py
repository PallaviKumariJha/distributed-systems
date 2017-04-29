#Author : Pallavi
#Created on : 7th March 2017
#Modified on : 

# Chor ring implementation

# all the master nodes in the chord architecture
masterNodes = {}
# For quick testing uncomment the following
# masterNodes = {16:[],32:[],45:[],80:[],96:[],112:[]}
# Comment out addMasterNodes() on line 59
# Uncomment createFingerTable(masterNodes) on line 189
# run the code.

nodesWithUserKeys = {}

def printFingerTable():
	keys = sorted(masterNodes.keys())
	val = sorted(masterNodes.values())

	print "\nNodes are: ", keys, "\n"
	print "Following is the finger table for nodes, Node: [Keys]\n"
	for key in keys:
		print key, ":", masterNodes[key]
	print ""

def createFingerTable(masterNodes):
	nodes = sorted(masterNodes.keys())
	totalNodes = len(masterNodes.keys())
	for key,value in masterNodes.iteritems():
		#clear the list before recreation
		masterNodes[key] = []
		nodesWithUserKeys[key] = []

		# Following is the formula to generate keys
		# id > n + 2^i (mod 2^m)
		# n = 16,32,45,80,96,112
		# i = ith entry -> 0 to 7
		# m = range of m is 0-128

		n = key
		i = 0
		for i in range(0,7): 
			result = (n + 2**i)
			if result > 128:
				result = result % 2**i
			j = 0
			while (result > nodes[j]):
				if j < totalNodes-1:
					j = j+1;
				else:
					j = 0
					break
			keyVal = nodes[j]
			masterNodes[n].append(keyVal)

	printFingerTable()

def addMasterNodes():
	print "How many nodes you want in chord ring"
	noOfNodesInRing = input()
	for x in xrange(0,noOfNodesInRing):
		print "Input a node"
		node = input()
		masterNodes[node] = []
		createFingerTable(masterNodes)


def delNode(node):
	del masterNodes[node]
	print "Deleted node: ", node,"\n"
	print "Finger table created after deletion of the code"
	createFingerTable(masterNodes)

def addNode(node):
	masterNodes[node] = []
	print "Added node: ", node,"\n"
	print "Finger table post addition"
	createFingerTable(masterNodes)

def lookupId(node, id, loopkUpFlag):
	global userNode
	path = []
	currentList = masterNodes[node]

	# firstCondition is (currentList[i] <= id) and (id < currentList[i+1])
	# let is be true initially since the finger table needs to be searched atleast once,
	# if it fails we will set firstCondition to false
	firstCondition = True
	sortedNodes = sorted(masterNodes.keys())
	noOfNodes = len(sortedNodes)
	firstNode = sortedNodes[0]
	lastNode = sortedNodes[noOfNodes-1]
	
	while firstCondition == True:
		flag = 0
		path.append(node)
		for i in range(len(currentList)-1):
			if ((currentList[i] <= id) and (id < currentList[i+1])):
				flag = 1
				node = currentList[i]
				currentList = masterNodes[node]
				break
		if flag == 1:
			firstCondition = True
		else:

			# check for the second condition
			if (node < id) and (id < currentList[0]):
				node = currentList[0]
				currentList = masterNodes[node]
				path.append(node)
				if(loopkUpFlag == 0):
					print "Node for given id:",id, "is: ", node
					print "path is: ",path,"\n"
					userNode = node
					firstCondition = False
				else:
					userNode = node
					firstCondition = False

			else:
 
				# if node is the last in the sorted order and
				# if key is beyond it 0
				if (((node == sortedNodes[noOfNodes-1]) and (id > node)) or ((node == sortedNodes[noOfNodes-1]) and (id < sortedNodes[0]))):
					node = sortedNodes[0]
					path.append(node)
					if (loopkUpFlag == 0):
						print "Node for given id:",id, "is: ", node
						print "path is: ",path,"\n"
						userNode = node
						firstCondition = False
					else:
						userNode = node
						firstCondition = False
				elif node == id:
					path.append(node)
					if (loopkUpFlag == 0):
						print "Node for given id:",id, "is: ", node
						print "path is: ",path,"\n"
						userNode = node
						firstCondition = False 
					else:
						userNode = node
						firstCondition = False
				else:
					noOfEntries = len(currentList)
					node = sorted(currentList)[noOfEntries-1]
					currentList = masterNodes[node]


def addNodeInput():
	print "Input a node to be added"
	node = input()
	addNode(node)

def delNodeInput():
	print "Input a node to be deleted"
	node = input()
	delNode(node)

def lookupIdInput():
	print "Input an ID to be found"
	id = input()
	print "Input the node from where the search should begin"
	node = input()
	lookupId(node,id,0)

def addAKey():
	# check if key is present or not
	i = 0
	flag = 0
	sortedKeys = sorted(masterNodes.keys())
	print "Input a key"
	userKey = input()
	lookupId(sortedKeys[0],userKey,1)
	 
	for x in nodesWithUserKeys[userNode]:
		if x == userKey:
			flag = 1
			print "Node", userNode, "already has the key\n"

	if flag == 0:
		nodesWithUserKeys[userNode].append(userKey)
		print "key added to", userNode, ":", nodesWithUserKeys[userNode], "\n"


# createFingerTable(masterNodes)
addMasterNodes()

choice = ""

if __name__ == '__main__':
	while choice != "exit":

		print "**********************************************"
		print "Input an option"
		print "1. Print the keys and finger table"
		print "2. Add a node"
		print "3. Delete a node"
		print "4. Lookup for a file ID"
		print "5. Add a key"
		print "**********************************************"


		choice = raw_input("What would you like to do\n")
		if choice == '1':
		    printFingerTable()
		elif choice == '2':
		    addNodeInput()
		elif choice == '3':
		    delNodeInput()
		elif choice == '4':
			lookupIdInput()
		elif choice == '5':
			addAKey()
		else:
		    print("That is not a valid input.")