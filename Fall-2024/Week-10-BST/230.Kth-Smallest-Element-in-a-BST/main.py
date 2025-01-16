def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    def helper(root):
        nonlocal k 
        nonlocal result
        if root == None or k == 0:
            return 
        helper(root.left)
        k -= 1
        if k == 0:
            result = root.val
        helper(root.right)

    result = 0
    #k already counter 
    helper(root)

    return result      