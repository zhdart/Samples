from collections import deque

class treeNode:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def append(self, value):
        if self.value == value:
            return False
        elif self.value > value:
            if self.left_child:
                return self.left_child.append(value)
            else:
                self.left_child = treeNode(value)
                return True
        else:
            if self.right_child:
                return self.right_child.append(value)
            else:
                self.right_child = treeNode(value)
                return True

    def search(self, value):
        if self.value == value:
            return True
        elif self.value > value:
            if self.left_child:
                return self.left_child.search(value)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.search(value)
            else:
                return False

    def get_value(self):
        return self.value
    
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

class BinarySearchTree:
    def __init__(self, value=None):
        self.root = None
        self.counter = 0
        if value != None:
            self.append(value)

    def append(self, value):
        self.counter+=1
        if self.root:
            return self.root.append(value)
        else:
            self.root = treeNode(value)
            return False

    def search(self, value):
        if self.root:
            return self.root.search(value)
        else:
            return False

    def get_right_child(self):
        return self.root.right_child
    
    def get_left_child(self):
        return self.root.left_child

    def get_value(self):
        return self.root.get_value()
    #Экспериментальные функции

    def __iter__(self):
        d = deque()
        self.tmp_root = self.root
        d.append(self.tmp_root)
        for i in range(self.counter):
            self.tmp_root=d[i]
            d[i] = self.tmp_root.get_value()
            if self.tmp_root.get_left_child() != None:
                d.append(self.tmp_root.get_left_child())
            if self.tmp_root.get_right_child() != None:
                d.append(self.tmp_root.get_right_child())
            yield d[i]

if __name__ == '__main__':
    tree = BinarySearchTree()
    for v in [8, 3, 10, 1, 6, 4, 14, 13, 7]:
        tree.append(v)

    for v in [8, 12, 13]:
        print(tree.search(v))
    for v in [8, 12, 13]:
        print(v in tree)
    print(*tree)