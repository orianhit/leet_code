# 1028. Recover a Tree From Preorder Traversal

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _from_subtree(self,traversal, c_split):
        c_split += '-'
        root = traversal.split(c_split)[0]
        passed_dash = False
        left_node_idx = None
        right_node_idx = None
        for idx, node in enumerate(traversal.split(c_split)[1:]):
            if node == '': # aka there is smaller dashes between the splits
                passed_dash = True
            elif '-' in node: # not exact dash count but may be later
                passed_dash = False
            elif not passed_dash: # if at least 1 step away from non-exact dash
                if left_node_idx is None: # set left b4 right
                    left_node_idx = idx + 1
                else:
                    right_node_idx = idx + 1
            else:
                passed_dash = False

        # no children
        if left_node_idx is None:
            return TreeNode(root, None, None)
        # both children
        if right_node_idx:
            left_node = self._from_subtree(c_split.join(traversal.split(c_split)[left_node_idx:right_node_idx]), c_split)
            right_node = self._from_subtree(c_split.join(traversal.split(c_split)[right_node_idx:]), c_split)
        # only left children
        else:
            right_node = None
            left_node = self._from_subtree(c_split.join(traversal.split(c_split)[left_node_idx:]), c_split)

        return TreeNode(root, left_node, right_node)

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        return self._from_subtree(traversal, '')


if __name__ == "__main__":
    sol = Solution()
    print(sol.recoverFromPreorder("10-4-2--9---6----6-----9--5"))
