class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        Adds the value to the tree as a node, or do nothing if already in the tree
        :param self: The tree
        :param value: value to add to tree
        :return: No Return
        """
        new_node = Node(value)
        if self.size == 0:                       # If the tree is empty
            self.root = new_node
            self.size += 1
        else:                                       # Tree isn't empty
            node = self.root
            while new_node.value != node.value:
                if new_node.value < node.value:     # Node to add is less then node
                    if node.left is None:
                        node.left = new_node
                        node.left.parent = node
                        self.size += 1
                    else:
                        node = node.left
                elif new_node.value == node.value:
                    return None
                else:                               # Node to add is greater then
                    if node.right is None:
                        node.right = new_node
                        node.right.parent = node
                        self.size += 1
                    else:
                        node = node.right

    def remove(self, value):
        """
        Removes node with matching value from tree, else does nothing
        When removing a node with two children, replace with the min of the right subtree
        :param self: The tree
        :param value: value to remove from tree
        :return: No Return
        """
        # CASE01: Tree doesn't exist
        if self.size < 1:
            return None
        node_to_rmv = self.search(value, self.root)

        # CASE02: Value isn't in the tree
        if node_to_rmv.value != value:
            return None

        # CASE03: Node being removed is a leaf
        if node_to_rmv.left is None and node_to_rmv.right is None:
            if node_to_rmv == self.root:
                node_to_rmv.value = None
                self.root = None
            else:
                if node_to_rmv.parent.left == node_to_rmv:
                    node_to_rmv.parent.left = None
                else:
                    node_to_rmv.parent.right = None
                node_to_rmv = None
            self.size -= 1

        # CASE04: Has one Left child
        elif node_to_rmv.left is not None and node_to_rmv.right is None:
            child = node_to_rmv.left
            if node_to_rmv != self.root:
                child.parent = None
            node_to_rmv.value = child.value
            node_to_rmv.left = child.left
            node_to_rmv.right = child.right
            self.size -= 1

        # CASE04: Has one Right child
        elif node_to_rmv.left is None and node_to_rmv.right is not None:
            child = node_to_rmv.right
            if node_to_rmv != self.root:
                child.parent = None
            node_to_rmv.value = child.value
            node_to_rmv.left = child.left
            node_to_rmv.right = child.right
            self.size -= 1

        # CASE05: Node being removed has two children
        # Node value is replaced by the successors, value, then successor is removed
        # The successor is the next largest node in the tree
        #  --> the right child's leftmost child
        else:
            child = self.min(node_to_rmv.right)
            node_to_rmv.value = child.value
            node_to_rmv.right.parent = node_to_rmv
            node_to_rmv.left.parent = node_to_rmv
            if node_to_rmv == self.root:
                if child.parent.left == child:
                    child.parent.left = None
                else:
                    child.parent.right = None
            else:
                if node_to_rmv == node_to_rmv.right:
                    node_to_rmv.right.parent = None
                    node_to_rmv.right = None
                elif node_to_rmv == node_to_rmv.left:
                    node_to_rmv.left.parent = None
                    node_to_rmv.left = None
            self.size -= 1

    def search(self, value, node):
        """
        Finds value in tree (recursive)
        :param self: The tree
        :param value: value to find in tree
        :param node: root of tree or subtree
        :return: Node with value, or potential parent
        """
        if self.root is not None:
            if value == node.value:
                return node
            elif value < node.value:
                if node.left is not None:
                    return self.search(value, node.left)
                else:
                    return node
            else:
                if node.right is not None:
                    return self.search(value, node.right)
                else:
                    return node
        else:
            return None

    def inorder(self, node):
        """
        Traverse tree using the in-order method (recursive)
        :param self: The tree
        :param node: starting node
        :return: generator object of the tree
        """
        if node is not None:
            if self.depth(node.value) != -1:
                if node.left is not None:
                    for i in self.inorder(node.left):
                        yield i
                yield node.value
                if node.right is not None:
                    for i in self.inorder(node.right):
                        yield i
            else:
                return None

    def preorder(self, node):
        """
        Traverse tree using the pre-order method (recursive)
        :param self: The tree
        :param node: starting node
        :return: generator object of the tree
        """
        if node is not None:
            if self.depth(node.value) != -1:
                if node == self.root:
                    yield node.value
                    self.preorder(node.parent)

                if node.left is not None:
                    yield node.left.value
                    for i in self.preorder(node.left):
                        yield i
                if node.right is not None:
                    yield node.right.value
                    for i in self.preorder(node.right):
                        yield i
            else:
                return None

    def postorder(self, node):
        """
        Traverse tree using the post-order method (recursive)
        :param self: The tree
        :param node: starting node
        :return: generator object of the tree
        """

        if node is not None:
            sz = self.depth(node.value)
            if sz != -1:
                if node.right is not None:
                    for i in self.postorder(node.left):
                        yield i
                if node.left is not None:
                    for i in self.postorder(node.right):
                        yield i
                yield node.value
            else:
                return None

    def depth(self, value):
        """
        finds the depth of the given node
        :param self: The tree
        :param value: value to find depth of
        :return: depth
        """
        if self.get_size() == 0:
            return -1
        node = self.search(value, self.root)
        if node.value != value:
            return -1
        depth = 0
        while node != self.root:
            depth += 1
            node = node.parent
        return depth

    def height(self, node):
        """
        Finds the height of the tree (recursive)
        :param self: The tree
        :param node: root node
        :return: height of the tree
        """
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def min(self, node):
        """
        Finds the min node of the tree (recursive)
        :param self: The tree
        :param node: root node
        :return: min node of the tree
        """
        if node is None:
            return
        if node.left is not None:
            node = node.left
            return self.min(node)
        else:
            return node

    def max(self, node):
        """
        Finds the max node of the tree (recursive)
        :param self: The tree
        :param node: root node
        :return: max node of the tree
        """
        if node is None:
            return
        if node.right is not None:
            node = node.right
            return self.max(node)
        else:
            return node

    def get_size(self):
        """
        Gets the # of nodes in the BST
        :param self: The tree
        :return: # of nodes in BST
        """
        return self.size

    def is_perfect(self, node):
        """
        If BST is perfect
        :param self: The tree
        :param node: root node
        :return: True if perfect, else False
        """
        if self.get_size() == 0:
            return True
        if node.left is not None and node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            if self.depth(self.min(self.root).value) == self.depth(self.max(self.root).value):
                return True
            else:
                return False
        elif node.left is not None and node.right is None:
            return False
        elif node.right is not None and node.left is None:
            return False

    def is_degenerate(self):
        """
        If BST is degenerate
        :param self: The tree
        :return: True if degenerate, else False
        """
        parent = self.root
        if parent is None:
            return False
        r_sub_tree = parent.right
        l_sub_tree = parent.left
        cnt = True
        while cnt:
            if r_sub_tree is not None:
                if l_sub_tree is not None:
                    return False
                parent = r_sub_tree
                r_sub_tree = parent.right
                l_sub_tree = parent.left
            elif l_sub_tree is not None:
                parent = l_sub_tree
                l_sub_tree = parent.left
                r_sub_tree = parent.right
            else:
                return True