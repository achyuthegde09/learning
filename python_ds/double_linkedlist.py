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
        while itr:
            print(itr.data, '-->')
            itr = itr.next

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