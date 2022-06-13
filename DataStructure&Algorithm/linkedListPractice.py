class makeLinkedList:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode
class linkedListMethod:
    def __init__(self, head=None, target_node=None):
        self.head = head
        self.target_node = target_node
    def insertValue(self, value):
        insert_node = makeLinkedList(value)
        if self.head is None:
            self.head = insert_node
            return
        current_node = self.head
        while True:
            if current_node.nextNode is None:
                current_node.nextNode = insert_node
                break
            current_node = current_node.nextNode
    def printLinkedList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node, "->", end=' ')
            current_node = current_node.nextNode
        print("None")
    def print_target_linked_list(self, target_node):
        current_node = self.target_node
        while current_node is not None:
            print(current_node, "->", end=" ")
            current_node = current_node.nextNode
        print("None")



node1 = makeLinkedList("7")
node2 = makeLinkedList("3")
node3 = makeLinkedList("991")
node1.nextNode = node2
node2.nextNode = node3
# print(f"node1 is {node1.value}, node1.next is {node1.nextNode}")
# print(f"node2 is {node2.value}, node2.next is {node2.nextNode}")
# print(f"node3 is {node3.value}, node3.next is {node3.nextNode}")
# print(node1.nextNode.nextNode.value)
linkedListMethod().print_target_linked_list(node1)

