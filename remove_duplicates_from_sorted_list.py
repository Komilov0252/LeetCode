
l = [1,2,2,3,3,4]

class ListNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode()
    def append(self, value):
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(value)
    def print(self):
        node = self.head.next
        while node:
            print(node.value, end = ' ')
            node = node.next
    def removeDuplicates(self):
        node = self.head.next
        while node:
            tmp = node.next
            while tmp:
                if node.value == tmp.value:
                    tmp = tmp.next
                else:
                    node.next = tmp
                    break
            node = node.next

            
            
        
        

ll = LinkedList()
for i in l:
    ll.append(i)
ll.removeDuplicates()
ll.print()