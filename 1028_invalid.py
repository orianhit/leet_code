from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        output_arr = []
        traversal_len = len(traversal)
        for dash_size in range(traversal_len):
            current_split = (traversal_len-dash_size) * '-'
            if not current_split:
                continue
            current_depth_children = traversal.split(current_split)
            if len(current_depth_children) == 1:
                continue

            curr_depth_array = []
            odd = True
            for current_depth_child in current_depth_children[1:]:
                current_depth_child_valid = current_depth_child.split('-')[0]
                # check if single child
                curr_depth_array.append(current_depth_child_valid)
                if odd and '-' in current_depth_child:
                    curr_depth_array.append(None)
                odd = not odd

            if len(curr_depth_array) % 2:
                curr_depth_array.append(None)

            for idx, current_depth_child in enumerate(current_depth_children[::-1][:-1]):
                real_idx = len(current_depth_children) - idx
                prev_len = len(current_split.join(current_depth_children[:real_idx - 1]))
                current_child_len = len(current_depth_child.split('-')[0])
                traversal = traversal[:prev_len] + traversal[prev_len + current_child_len + len(current_split):]

            output_arr = curr_depth_array + output_arr
        output_arr = [traversal] + output_arr
        return output_arr if output_arr[-1] else output_arr[:-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.recoverFromPreorder("1-2--3--4-5--6--7"))