def preorder(self, root: 'Node'):
    if root == None:
        return []
    node_list = []
    val_list = []
    current_node = root
    while True:
        node_list += current_node.children[::-1]
        val_list.append(current_node.val)
        if len(node_list) == 0:
            return val_list
        current_node = node_list.pop()
