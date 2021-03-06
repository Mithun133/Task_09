class Node:
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def get_length(self):
        count = 0
        n = self.head
        while n:
            count = count + 1
            n = n.next
            return count

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

    def search(self,search_item):
        n = self.head.next

        while n !=None:
            if n.data == search_item:
                print('\n Data found in link list.')
                return
            n = n.next
        print('\n data not found') 



if __name__ == '__main__':
    ll = LinkedList()
    print("\nAdded elements at begining : ")
    ll.insert_at_beginning(50)
    ll.insert_at_beginning(100)
    ll.insert_at_beginning(150)
    ll.insert_at_beginning(200)
    ll.insert_at_beginning(250)
    ll.insert_at_beginning(500)
    ll.print_link_list()


    ll.search(150)
    ll.search(1000)



class Node:
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def get_length(self):
        count = 0
        n = self.head
        while n:
            count = count + 1
            n = n.next
            return count

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

    def search(self,search_item):
        n = self.head.next

        while n !=None:
            if n.data == search_item:
                print('\n Data found in link list.')
                return
            n = n.next
        print('\n data not found') 



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


    ll.search(5)
    ll.search(22)

class Node:
    def __init__(self, data= 'Head', next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def get_length(self):
        count = 0
        n = self.head
        while n:
            count = count + 1
            n = n.next
            return count

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

    def search(self,search_item):
        n = self.head.next

        while n !=None:
            if n.data == search_item:
                print('\n Data found in link list.')
                return
            n = n.next
        print('\n data not found') 



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


    ll.search(50)
    ll.search(100)