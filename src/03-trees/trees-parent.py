"""
Implementation of Binary Trees with parent pointer
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.parent = None # points to the predecessor
        self.left = None # points to the left leaf
        self.right = None # points to the right leaf

    def __eq__(self, other):
        return self.value == other.value
    
class BinaryTree():
    def __init__(self):
        self._root = None 

    "METHODS ARE IMPLEMENTED WITH RECURSION"

    def size(self) -> int:
        "For calculating the number of nodes"
        return self._size(self._root)
        
    def _size(self, node: Node):
        "Recursive method (where calculations are done) for size()"
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right) # head + recursive to left + recursive to right
        
    def height(self):
        "Returns the total height of the tree"
        return self._height()

    def _height(self, node: Node):
        if node is None:
            return 0
        # we want to obtain the maximum possible number between left and right
        return 1 + max(self._height(node.left), self._height(node.right))

    def depth(self, node):
        "Gives the depth of a node"
        if node is None:
            return 0
        if node.parent is None: # root node
            return 0
        # instead of going from the root -> down; we do down -> root
        return 1 + self.depth(node.parent)

    def preorder(self):
        """prints the preorder (root, left, right) traversal of the tree"""
        return self._preorder(self._root)

    def _preorder(self, node):
        if node is None:
            return 
        print(node.value)
        self._preorder(node.left)
        self._preorder(node.right)
        return 1
    
    # postorder is (root, right, left) --- just change a the line order when printing
    
    def inorder(self):
        """prints the inorder (left, root, right)  traversal of the tree"""
        return self._inorder(self._root)
    
    def _inorder(self, node):
        if node is None:
            return 0
        self._inorder(node.left)
        print(node.value)
        self._inorder(node.right)


    def draw(self):
        "For printing the tree, useful for debug"
        if self._root:
            self._draw("    ", self._root, False)
        else:
            print("tree is empty")
        print("\n\n")

    def _draw(self, prefix:str, node:Node, is_left: bool):
        if node is not None:
            self._draw(prefix + "   ", node.right, False)
            print(prefix + "|-- " + str(node.value))
            self._draw(prefix + "   ", node.left, True)


"""As you can see, node.parent is kinda useless. You can perfectly do this algorithms without 
node.parent (depth can be reformulated)."""

node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")
node6 = Node("6")

node1.right = node5
node1.left = node2
node2.left = node3
node2.right = node4
node5.right = node6

node2.parent = node1
node5.parent = node1
node3.parent = node2
node4.parent = node2
node6.parent = node5

myTree = BinaryTree()
myTree._root = node1
print(f"The tree in {myTree} has a size of {myTree.size()}\n")
myTree.draw()
myTree.inorder()