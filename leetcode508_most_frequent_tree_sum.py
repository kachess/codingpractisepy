#%%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        _stat = dict()
        def getTreeSum(root):
            if not root:
                return 0
            else:
                sofarsum = getTreeSum(root.left) + root.val  + getTreeSum(root.right)
                if sofarsum in _stat:
                    _stat[sofarsum] = _stat[sofarsum] +1
                else:
                    _stat[sofarsum] = 1
            return sofarsum

        res = []
        getTreeSum(root)
        vmax = max(_stat.values())
        for k, v in _stat.items():
            if v == vmax:
                res.append(k)
        return res
