"""
This module provides a solution to the problem of removing all occurrences of a
specific value from an array in-place and returning the new length of the array 
without those elements. The order of elements can be changed, and the algorithm 
ensures that the first k elements of the array do not include the specified value, where k 
is the new length of the array.

The solution is implemented within the Solution class, which contains the method remove_element. 
This method applies a two-pointer technique to achieve in-place removal with O(n) time complexity 
and O(1) space complexity, where n is the number of elements in the array.

Constraints:
- The length of the array nums is in the range [0, 100].
- The values of the elements in nums range from 0 to 50.
- The value to remove, val, is in the range [0, 100].

Example Usage:
>>> solution = Solution()
>>> nums = [3, 2, 2, 3]
>>> val = 3
>>> k = solution.remove_element(nums, val)
>>> print(k)
2
>>> print(nums[:k])
[2, 2]
"""

from typing import List

class Solution:
    """
    This class offers a solution to removing all occurrences of a specific value from an array.
    The class's primary method, `remove_element`, modifies the input array in-place to exclude
    all instances of the specified value and returns the count of the remaining elements.
    This approach is designed to fulfill requirements where the order of elements can be altered
    and only the elements not equal to a specified value are kept in the beginning of the array.
    
    The solution employs a two-pointer technique to achieve in-place modification
    with optimal time and space complexity.
    """
    def remove_element(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of a specified value in-place within an array and returns 
        the new length of the array without those elements.

        Parameters:
        - nums (List[int]): The input array of integers from which occurrences of 
        'val' will be removed.
        - val (int): The value to be removed from the array.

        Returns:
        - int: The new length of the array after removing all occurrences of 'val'. 
        This is also the number of elements in the array that are not equal to 'val'.

        The function modifies the input array 'nums' in-place, moving all elements
        not equal to 'val' to the beginning of the array. The order of these 
        elements is maintained, but the order of the removed elements does not matter.
        The space beyond the new length of the array (k) is not guaranteed to be in any 
        particular order or state.

        This approach uses a two-pointer technique where one pointer (insert_pos) tracks
        the position at which the next non-'val' element should be placed, and the other
        pointer iterates through the array. This ensures an O(n) time complexity, where n
        is the number of elements in the array, and an O(1) space complexity since no
        additional storage is needed.
        """
        # Initialize the insert position for non-val elements.
        insert_pos = 0
        # Iterate through each element in the array.
        for num in nums:
            # If the current element is not equal to val,
            # place it at the current insert position and increment the insert position.
            if num != val:
                nums[insert_pos] = num
                insert_pos += 1
        # Return the new length of the array after removing val elements.
        return insert_pos
