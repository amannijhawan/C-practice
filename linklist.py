class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class List(object):
    def __init__(self, data=None):
        try:
            node = Node(None, None)
            for item in data:
                node=Node(item, node)
            self.data = node
        except:
            self.data = data
    def insert(self, data):
        node = Node(data, self.data)
        self.data = node

    def delete(self, node):
        for _node in self.data:
            if _node.next == node:
                _node.next = node.next
                del node
                return
        raise Exception("Node not found");

    def __str__(self):
        output = ''
        node = self.data
        while node:
            output = '%s %s' % (output, node)
            node = node.next
        return output
        
    def __iter__(self):
        node = self.data
        while node:
            yield node
            node = node.next
        raise StopIteration
            
if __name__ == '__main__':
    list1= List([10,9,1231])
    for item in xrange(10):
        list1.insert(item)
    for item in list1:
        print item


