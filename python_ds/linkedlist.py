class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('LinkedList is empty')
            return
        itr = self.head
        print_str = ''
        while itr:
            print_str += str(itr.data) + ' --> '
            itr = itr.next
        print(print_str)

    def insert_at_end(self, data):
        new = Node(data, None)
        if self.head is None:
            self.head = new
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = new

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

        itr = self.head
        for i in range(index - 1):
            itr = itr.next
        itr.next = itr.next.next

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
        itr.next = new_node

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        new_node = Node(data_to_insert, None)
        while itr:
            if itr.data == data_after:
                new_node.next = itr.next
                itr.next = new_node
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if data == self.head.data:
            self.head = self.head.next
            return

        prev = self.head
        itr = self.head.next
        while itr:
            if itr.data == data:
                prev.next = itr.next
            prev = itr
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begin(102)
    ll.insert_at_begin(12121)
    ll.insert_at_end(125)
    ll.print()
    new_list = [12,4545,1212,6422,56662,11456]
    ll.insert_values(new_list)
    print("new one")
    ll.print()
    print(ll.get_length())
    ll.remove_at(2)
    ll.print()
    ll.insert_at(5, 10101)
    ll.print()
    ll.insert_after_value(10102, 144)
    ll.print()
    ll.insert_after_value(10102, 144)
    ll.print()
    ll.remove_by_value(12)
    ll.print()
    ll.remove_by_value(10101)
    ll.print()
