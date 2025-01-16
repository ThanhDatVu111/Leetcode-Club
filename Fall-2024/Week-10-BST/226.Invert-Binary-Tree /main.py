def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root: #base case to return when we go down each node to go back up
        return None
    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root