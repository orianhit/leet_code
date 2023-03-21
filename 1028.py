# 1028. Recover a Tree From Preorder Traversal

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        return self._from_subtree(traversal, '')

    def _from_subtree(self, traversal, c_split):
        c_split += '-'
        root = traversal.split(c_split)[0]
        passed_dash = False
        left_node_idx = None
        right_node_idx = None

        # after the first element which is current root
        for idx, node in enumerate(traversal.split(c_split)[1:]):
            # (1) --43
            if node == '':  # aka there is smaller leaf (more dashes) between the splits
                passed_dash = True
            # (2) --43---55--43
            elif '-' in node:  # not exact dash count but later may be
                passed_dash = False
            elif not passed_dash:  # found valid node
                if left_node_idx is None:  # setting left b4 setting right
                    left_node_idx = idx + 1
                else:
                    right_node_idx = idx + 1
            else:
                passed_dash = False

        # no children - create leaf
        if left_node_idx is None:
            # break from recursion
            return TreeNode(root, None, None)
        # both children
        if right_node_idx:
            # left node from its start position to right start position
            left_node = self._from_subtree(
                c_split.join(traversal.split(c_split)[left_node_idx:right_node_idx]),
                c_split)
            # right node from its start position to the end
            right_node = self._from_subtree(
                c_split.join(traversal.split(c_split)[right_node_idx:]), c_split)
        # only left children
        else:
            right_node = None
            # left node from its start position to the end
            left_node = self._from_subtree(
                c_split.join(traversal.split(c_split)[left_node_idx:]),
                c_split)

        return TreeNode(root, left_node, right_node)


if __name__ == "__main__":
    sol = Solution()
    print(sol.recoverFromPreorder("10-4-2--9---6----6-----9--5"))
