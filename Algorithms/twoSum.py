from typing import List

class Solution:
    """
    A class used to represent the solution for finding two indices in a list that add up to a target sum.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

        Parameters
        ----------
        nums : List[int]
            List of integers.
        target : int
            The target sum.

        Returns
        -------
        List[int]
            Indices of the two numbers that add up to `target`. If no such numbers exist, returns an empty list.
        """
        # Dictionary to store the value and its index
        num_to_index = {}
        
        # Iterate over the list of numbers
        for i, num in enumerate(nums):
            # Calculate the value needed to reach the target
            find_remaining_value = target - num
            # Check if the needed value is already in the dictionary
            if find_remaining_value in num_to_index:
                # If found, return the indices of the two numbers
                return [num_to_index[find_remaining_value], i]
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = i
        
        # Return an empty list if no solution is found
        return []