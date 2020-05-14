from node import Node
import hashlib, pickle, json

def createTree(listOfValues):
    if len(listOfValues)>1:
        left = createTree(listOfValues[0:int(len(listOfValues)/2)])
        right = createTree(listOfValues[int(len(listOfValues)/2):])
        dataHash = getHash(left.hashVal+right.hashVal)
        n = Node()
        #print("new")
        n.lchild = left
        n.rchild = right
        n.hashVal = dataHash
        print(n.toJson())
    else:
        n = Node()
        n.hashVal = listOfValues[0]
        print(n.toJson())
    return n

def treeToString(node,treeString=[]):
    if node.lchild:
        treeString = treeToString(node.lchild,treeString)
        treeString.append(node.hashVal)
        treeString = treeToString(node.rchild,treeString)
    else:
        return treeString+[node.hashVal]
    #print(len(treeString))
    return treeString

def getHash(s):
    chunkBytes = pickle.dumps(s)
    chunkHash = hashlib.sha256(chunkBytes).hexdigest()
    return chunkHash
    
inputData = "Hello World. It is a beautiful day!"
chunkSize = int(len(inputData)/8)
dataChunks = []
for i in range(0,len(inputData),chunkSize):
    chunkHash = getHash(inputData[i:i+chunkSize])
    dataChunks.append(chunkHash)

# Adjust length of data to be even for a balanced tree
if len(dataChunks)%2 != 0:
    dataChunks.append(dataChunks[-1])
result = createTree(dataChunks)
stringResult = treeToString(result)
print("Final : ", stringResult)
