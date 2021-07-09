class Node:
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_link_list(self):
        if self.head.next is None:
            print('Linked list is empty.')
            return

        current_node = self.head
        res_str = ''
        while current_node != None:
            res_str = res_str + str(current_node.data) + ' ----> '
            current_node = current_node.next

        print(res_str)
    # --------------------------remove--------------
    def remove(self, x):
        if self.head is None:
            print("Can't delete because LL is empty.")
            return


if __name__ == '__main__':
    ll = LinkedList()
    print("\nAdded elements at begining : ")
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(40)
    ll.insert_at_beginning(50)
    ll.insert_at_beginning(60)
    ll.print_link_list()





class Node:
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_link_list(self):
        if self.head.next is None:
            print('Linked list is empty.')
            return

        current_node = self.head
        res_str = ''
        while current_node != None:
            res_str = res_str + str(current_node.data) + ' ----> '
            current_node = current_node.next

        print(res_str)
    # --------------------------remove--------------
    def remove(self, x):
        if self.head is None:
            print("Can't delete because LL is empty.")
            return


if __name__ == '__main__':
    ll = LinkedList()
    print("\nAdded elements at begining : ")
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(40)
    ll.insert_at_beginning(60)
    ll.insert_at_beginning(80)
    ll.insert_at_beginning(100)
    ll.insert_at_beginning(120)
    ll.print_link_list()



class Node:
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_link_list(self):
        if self.head.next is None:
            print('Linked list is empty.')
            return

        current_node = self.head
        res_str = ''
        while current_node != None:
            res_str = res_str + str(current_node.data) + ' ----> '
            current_node = current_node.next

        print(res_str)
    # --------------------------remove--------------
    def remove(self, x):
        if self.head is None:
            print("Can't delete because LL is empty.")
            return


if __name__ == '__main__':
    ll = LinkedList()
    print("\nAdded elements at begining : ")
    ll.insert_at_beginning(100)
    ll.insert_at_beginning(200)
    ll.insert_at_beginning(300)
    ll.insert_at_beginning(400)
    ll.insert_at_beginning(500)
    ll.insert_at_beginning(600)
    ll.print_link_list()


class Node:
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_link_list(self):
        if self.head.next is None:
            print('Linked list is empty.')
            return

        current_node = self.head
        res_str = ''
        while current_node != None:
            res_str = res_str + str(current_node.data) + ' ----> '
            current_node = current_node.next

        print(res_str)
    # --------------------------remove--------------
    def remove(self, x):
        if self.head is None:
            print("Can't delete because LL is empty.")
            return


if __name__ == '__main__':
    ll = LinkedList()
    print("\nAdded elements at begining : ")
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(40)
    ll.insert_at_beginning(50)
    ll.insert_at_beginning(60)
    ll.print_link_list()


class Node:
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_link_list(self):
        if self.head.next is None:
            print('Linked list is empty.')
            return

        current_node = self.head
        res_str = ''
        while current_node != None:
            res_str = res_str + str(current_node.data) + ' ----> '
            current_node = current_node.next

        print(res_str)
    # --------------------------remove--------------
    def remove(self, x):
        if self.head is None:
            print("Can't delete because LL is empty.")
            return


if __name__ == '__main__':
    ll = LinkedList()
    print("\nAdded elements at begining : ")
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(15)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(25)
    ll.insert_at_beginning(30)
    ll.print_link_list()