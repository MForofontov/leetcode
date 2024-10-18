from typing import List
from itertools import combinations

class Solution:
    """
    A class used to represent the solution for counting the number of subsets that achieve the maximum OR value.

    Methods
    -------
    countMaxOrSubsets(nums: List[int]) -> int
        Returns the number of subsets that achieve the maximum OR value.
    """
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        Returns the number of subsets that achieve the maximum OR value.

        Parameters
        ----------
        nums : List[int]
            List of integers.

        Returns
        -------
        int
            The number of subsets that achieve the maximum OR value.
        """
        # Step 1: Calculate the maximum possible OR by OR-ing all elements
        max_or: int = 0
        for num in nums:
            max_or |= num

        # Step 2: Count how many subsets achieve the maximum OR
        n: int = len(nums)
        count: int = 0

        # Iterate over all possible subsets
        for i in range(1, n + 1):
            for subset in combinations(nums, i):
                subset_or: int = 0
                for num in subset:
                    subset_or |= num
                if subset_or == max_or:
                    count += 1

        return count