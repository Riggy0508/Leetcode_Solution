// https://leetcode.com/problems/inorder-successor-in-bst

#If you know inorder traversal and the properties of BST this is a super easy problem

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        suc=None
        
        while root:
            if p.val>=root.val:
                root=root.right
            else:
                suc=root
                root=root.left
                
        return suc