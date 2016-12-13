class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def printAllVals(self):
        runner = self.head
        while runner:
            print(runner.value)
            runner = runner.next
        return self

    def addBack(self, value):
        runner = self.head
        while runner:
            if not runner.next:
                runner.next = Node(value)
                break
            runner = runner.next

    def addFront(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def insertBefore(self, nextVal, value):
        newNode = Node(value)
        runner = self.head
        while runner:
            if runner.next.value == nextVal:
                newNode.next = runner.next
                runner.next = newNode
                break
            runner = runner.next

    def insertAfter(self, preVal, value):
        newNode = Node(value)
        runner = self.head
        while runner:
            if runner.value == preVal:
                newNode.next = runner.next
                runner.next = newNode
                break
            runner = runner.next

    def removeNode(self, value):
        runner = self.head
        while runner:
            if not runner.next.next:
                runner.next = runner.next.next
                break
            runner = runner.next

    def reverseList(self):
        prev = None
        current = self.head
        count = 0
        while current is not None:

            next = current.next
            current.next = prev
            prev = current
            current = next

            # count += 1
            # print (count)
        self.head = prev

list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')

list.printAllVals()
list.addBack('Ben')
list.addFront('Aaron')
list.insertBefore('Debra','Caleb')
list.insertAfter('Chad','John')
list.removeNode('Alice')

list.printAllVals()

print ('**REVERSE**')
list.reverseList()
list.printAllVals()
