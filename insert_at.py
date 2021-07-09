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

    def insert_at(self,position,data):
    
        if self.head.next == None:
            #self.add_begining(data)
            new_node = Node(data)
            new_node.next = self.head

            self.head = new_node

        cnt = 0
        n = self.head
        while n != None:
            if cnt == position - 1:
                node = Node(data, n.next)
                n.next = node
                break
            n = n.next
            cnt = cnt + 1



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


    print("\n\nAfter inserting element: ")
    ll.insert_at(2, 100)
    ll.insert_at(4, 400)
    ll.print_link_list()




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

    def insert_at(self,position,data):
    
        if self.head.next == None:
            #self.add_begining(data)
            new_node = Node(data)
            new_node.next = self.head

            self.head = new_node

        cnt = 0
        n = self.head
        while n != None:
            if cnt == position - 1:
                node = Node(data, n.next)
                n.next = node
                break
            n = n.next
            cnt = cnt + 1



if __name__ == '__main__':
    ll = LinkedList()
    print("\nAdded elements at begining : ")
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(15)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(25)
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(35)
    ll.insert_at_beginning(40)
    ll.print_link_list()


    print("\n\nAfter inserting element: ")
    ll.insert_at(2, 37)
    ll.insert_at(7, 18)
    ll.print_link_list()



