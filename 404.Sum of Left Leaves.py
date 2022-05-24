
def sumOfLeftLeaves(root) -> int:
    sum_of_left = 0

    def check_left(node, is_left):
        global sum_of_left
        if (node == None):
            return
        if is_left & (node.left == None) & (node.right == None):
            sum_of_left = sum_of_left + node.val
        check_left(node.left, True)
        check_left(node.right, False)

    check_left(root, False)
    return sum_of_left