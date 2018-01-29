class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return [[]]
        q1 = [root]
        q2 = []
        res = []
        flip = 0
        while len(q1) > 0:
            tmp = []
            if flip:
                for i in range(len(q1)).__reversed__():
                    tmp.append(q1[i].val)
                flip = 0
            else:
                for i in range(len(q1)):
                    tmp.append(q1[i].val)
                flip = 1
            res.append(tmp)
            for node in q1:
                if node.left != None:
                    q2.append(node.left)
                if node.right != None:
                    q2.append(node.right)
            q1 = q2
            q2 = []
        return res
