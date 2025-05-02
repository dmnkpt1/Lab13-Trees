def tree_by_levels(node):
    if node is None:
        return list()
    result = []

    l1 = [node]
    while l1:
        n = l1.pop(0)
        if n is None:
            continue
        result.append(n.value)
        if n.left:
            l1.append(n.left)
        if n.right:
            l1.append(n.right)

    return result
