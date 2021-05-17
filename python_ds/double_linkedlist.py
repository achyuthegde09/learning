class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data, None, None)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def print_fwd(self):
        if self.head is None:
            print('LinkedList is empty')
            return
        itr = self.head
        print_str = ''
        while itr:
            print_str += str(itr.data) + ' <-> '
            itr = itr.next
        print(print_str)

    def find_last_node(self):
        if self.head is None:
            print('LinkedList is empty')
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        itr = self.find_last_node()
        print_str = ''
        while itr:
            print_str += str(itr.data) + ' <-- '
            itr = itr.prev
        print(print_str)

    def insert_at_end(self, data):
        new = Node(data, None, None)
        if self.head is None:
            self.head = new
        else:
            end_node = self.find_last_node()
            new.prev = end_node
            end_node.next = new

    def insert_values(self, data_list):
        self.head = None
        for itr in data_list:
            self.insert_at_end(itr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr != None:
            itr = itr.next
            count += 1
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None

        itr = self.head
        for i in range(index - 1):
            itr = itr.next
        itr.next = itr.next.next
        itr.next.prev = itr

    def insert_at(self, index, value):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begin(value)
            return

        new_node = Node(value, None)
        itr = self.head
        for i in range(index - 1):
            itr = itr.next
        new_node.next = itr.next
        new_node.prev = itr
        itr.next = new_node
        new_node.next.prev = new_node


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begin(102)
    ll.insert_at_begin(12121)
    ll.insert_at_begin(121)
    ll.insert_at_begin(12)
    ll.print_fwd()
    ll.print_backward()
    ll.insert_at_end(78)
    ll.print_fwd()
    ll.remove_at(3)
    ll.print_fwd()
    ll.print_backward()

    ll.print_fwd()
    ll.insert_at(2, 95)
    ll.print_fwd()
    ll.print_backward()

