class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        self.__next_node = node

    def __repl__(self):
        return self.value

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head, self.tail = new_node, new_node

    def __len__(self):
        count = 0
        if self.head:
            count += 1
            if current := self.head.next_node:
                while current:
                    count += 1
                    current = current.next_node
        return count

    def remove_head(self):
        if self.head:
            value = self.head.value
            if self.head.next_node:
                self.head = self.head.next_node
            else:
                self.head, self.tail = None, None
            return value
        else:
            return None

    def remove_tail(self):
        if self.head:
            if self.head.next_node:
                current = self.head
                while current.next_node is not self.tail:
                    current = current.next_node
                value = current.next_node.value
                current.next_node = None
                self.tail = current
                return value
            else:
                return self.remove_head()
        else:
            return None

    def contains(self, value):
        if not self.head:
            return False

        def search(node):
            if node.value == value:
                return True
            if not node.next_node:
                return False
            return search(node.next_node)
        return search(self.head)

    def get_max(self):
        if not self.head:
            return None
        if not self.head.next_node:
            return self.head.value

        def return_max(node1, node2):
            if not node2.next_node:
                return max(node1.value, node2.value)
            else:
                return max(node1.value, return_max(node2, node2.next_node))
        return return_max(self.head, self.head.next_node)


# print(ll.remote_tail())
