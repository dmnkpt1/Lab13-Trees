# Pre-order traversal
def pre_order(node):
    result = []

    def pre_rec(node):
        if node is None:
            return
        result.append(node.data)
        pre_rec(node.left)
        pre_rec(node.right)

    pre_rec(node)
    return result

# In-order traversal
def in_order(node):
    result = []

    def in_rec(node):
        if node is None:
            return
        in_rec(node.left) 
        result.append(node.data)
        in_rec(node.right)

    in_rec(node)
    return result

# Post-order traversal
def post_order(node):
    result = []

    def post_rec(node):
        if node is None:
            return
        post_rec(node.left) 
        post_rec(node.right)
        result.append(node.data)

    post_rec(node)
    return result

