# 前序遍历
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# 后序遍历


def preorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRootVal())

# 中序遍历


def preorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        print(tree.getRootVal())
        preorder(tree.getRightChild())
