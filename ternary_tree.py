import random

class Node(object):
    def __init__(self, data, left=None, right=None, center=None):
        self.data = data
        self.left = left
        self.right = right
        self.center = center

    def __repr__(self):
        return 'Node <%d>' % (self.data)



# For easier usage below

right = 'right'
left = 'left'
center = 'center'


class TTree(object):
    '''
    Trinary Search Tree object
    '''
    def __init__(self, root=None):
        if root is not None:
            self.root = Node(root)
        else:
            self.root = None

    def insert(self, data, root=None, parent=None, child=None):
        if data is None:
            raise Exception

        if self.root is None:
            self.root = Node(data)
            return

        if root is None:
            root = self.root

        if data > root.data:
            if root.right is not None:
                self.insert(data, root.right)
            else:
                root.right = Node(data)

        if data < root.data:
            if root.left is not None:
                self.insert(data, root.left)
            else:
                root.left = Node(data)

        if data == root.data:
            if root.center is not None:
                self.insert(data, root.center)
            else:
                root.center = Node(data)

    def delete(self, data, root=None, parent=None, child=None):
        if not self.root:
            raise Exception("Empty Tree")

        if data is None:
            raise Exception("Data is None")

        if root is None:
            root = self.root

        if data > root.data:
            # Look in the right subtree
            if root.right:
                self.delete(data=data, root=root.right, parent=root,
                    child=right)
            else:
                raise Exception("Data Not Found")

        elif data < root.data:
            # Look in the left subtree
            if root.left:
                self.delete(data=data, root=root.left, parent=root, child=left)
            else:
                raise Exception("Data Not Found")

        else:
            # If the tree has more than one copy delete that first
            if root.center is not None:
                self.delete(data = data, root=root.center, parent=root, 
                    child=center)
            else:
            # Find the max node in my left subtree
            # Actually just setting root = None will not work
            # So we need an explicit reference to the parent node
                if child == center:
                    setattr(parent, child, None)

                lst_max_node = self.find_max_node(root.left)
                if lst_max_node is None:
                    if parent:
                        setattr(parent, child, None)
                    else:
                        self.root = root.right

                else:
                    root.data = lst_max_node.data
                    root.center = lst_max_node.center
                    # Remove all occurances of lst_max so set its center to None
                    lst_max_node.center = None
                    self.delete(data=lst_max_node.data, root=root.left,
                        parent=root, child=left)
    
    def find_max_node(self,root):
        if not root:
            return None
        while root.right is not None:
            root = root.right
        return root

    def traverse_inorder(self, root=None):
        if self.root is None:
            print "No Items to iterate on because Tree is empty "
            return
        if root is None:
            root = self.root
        if root.left:
            self.traverse_inorder(root=root.left)
        print root
        if root.center:
            self.traverse_inorder(root=root.center)
        if root.right:
            self.traverse_inorder(root=root.right)


def test_ttree():       
    ttree = TTree()
    for item in [5, 4, 9, 5, 7, 2, 2, 2,]:
        ttree.insert(item)

    ttree.delete(2)
    ttree.delete(2)
    ttree.delete(9)
    ttree.delete(5)
    ttree.delete(5)
    ttree.delete(4)
    ttree.delete(7)
    ttree.delete(2)

    #Should print empty Tree
    ttree.traverse_inorder()

    for item in range(100):
        ttree.insert(item)
    for item in range(100):
        ttree.insert(item)
    for item in range(100):
        ttree.delete(item)
    for item in range(100):
        ttree.delete(item)

    # Should print empty Tree
    ttree.traverse_inorder()

    # for item in [1]*100:
    #     ttree.insert(item)

    # for i in range(100):
    #     ttree.delete(1)
    # Should print empty Tree
    ttree.traverse_inorder()
    # Lets Test with some random data,
    for i in range(10000):
        try:
            random_data = []
            for i in range(10):
                random_data.append(random.randint(1,100))
                ttree.insert(random_data[-1])
            # import pdb;pdb.set_trace()
            for i in range(10):
                ttree.delete(ttree.root.data)
            if ttree.root:
                print "Test case Fail"
        except AttributeError:
            print "Test case fail"
    # Should print empty Tree
    print "Big Test case finished"
if __name__ == '__main__':
    test_ttree()
# ttree.traverse_inorder()
# import pdb; pdb.set_trace()