# binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Btree:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        temp = Node(data)

        if self.head == None:
            self.head = temp
            return

        tnode = self.head

        while True:

            if data < tnode.data:
                if tnode.left == None:
                    tnode.left = temp
                    return
                else:
                    tnode = tnode.left
                    continue
            
            if data > tnode.data:
                if tnode.right == None:
                    tnode.right = temp
                    return
                else:
                    tnode = tnode.right
                    continue

    def print(self, node):
        # To do this witout recursion, a stack needs to be used. https://www.geeksforgeeks.org/iterative-preorder-traversal/
        if node == None:
            return
        
        print(node.data)
        self.print(node.left)
        self.print(node.right)

    def printTree(self):
        self.print(self.head)

    def printcolumn(self):
        if not self.head:
            return

        queue = []
        queue.append(self.head)

        while queue:
            length = len(queue)
            for i in range(length):
                item = queue.pop(0)
                print(item.data, end = ' ')
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)

            print("")

    def getMin(self, root):
        temp = root
        while temp.left:
            temp = temp.left

        return temp

    def delNode(self, root, data):
        if not root:
            return None
        
        if data < root.data:
            root.left = self.delNode(root.left, data)
        elif data > root.data:
            root.right = self.delNode(root.right, data)
        else:
            if root.left == None and root.right == None:
                #leaf node
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                # both nodes are available, take in order successor (minimum node in right tree)
                temp = self.getMin(root.right)
                root.data = temp.data

                root.right = self.delNode(root.right, temp.data)

        return root
            
    def deleteNode(self, data):
        self.delNode(self.head, data)


tree = Btree()
tree.add(10)
tree.add(5)
tree.add(15)
tree.add(4)
tree.add(6)
tree.add(11)
tree.add(16)
tree.add(3)


tree.printcolumn()

tree.deleteNode(5)

print("   ")
tree.printcolumn()




