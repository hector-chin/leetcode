class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class linkedList:
    def __init__(self, head=None):
        self.head = head
    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end=' ')
            currentNode = currentNode.nextNode
        print("None")
    # def remove_specific_node(self, index, value):
    #     execute_times = 0
    #     currentNode = self.head
    #     while True:
    #         if execute_times < index - 1:
    #             currentNode = currentNode.nextNode
    #             execute_times += 1

    def insert_specific_index(self, index, value):
        currentNode = self.head
        new_node = linkedListNode(value)
        node_list = []
        while currentNode is not None:
            node_list.append(currentNode)
            try:
                temp_next_node = currentNode.nextNode
                currentNode = temp_next_node
            except:
                break

        node_list = node_list[0:index-1] + [new_node] + node_list[index - 1:]
        for i in range(0, len(node_list)):
            node_list[i].nextNode = None

        for i in range(0, len(node_list) - 1):
            print(type(node_list[i]))
            currentNode = node_list[i]
            currentNode.nextNode = node_list[i + 1]






ll = linkedList()
ll.printLinkedList()
ll.insert("3")
ll.printLinkedList()
ll.insert("44")
ll.printLinkedList()
ll.insert("55")
ll.printLinkedList()
ll.insert_specific_index(1, '9999')
# ll.printLinkedList()
