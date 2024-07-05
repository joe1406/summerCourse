#pre order:

def pre_order_traversal(node):
    print(node.data)
    if node.left not None:
        pre_order_traversal(node.left)
    if node.right not None:
        pre_order_traversal(node.right)

#post order:
        
def post_order_traversal(node):
    if node.left not None:
        post_order_traversal(node.left)
    if node.right not None:
        post_order_traversal(node.right)
    print(node.data)