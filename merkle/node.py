class Node:

    def __init__(self):
        self.lchild = None
        self.rchild = None
        self.hashval = None

    def toJson(self):
        try:
            result = {'lchild':self.lchild.hashVal, 'rchild':self.rchild.hashVal, 'hashVal':self.hashVal}
        except:
            result = {'lchild':None,'rchild':None, 'hashVal':self.hashVal}
        return result
