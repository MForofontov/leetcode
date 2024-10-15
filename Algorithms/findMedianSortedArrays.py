import statistics
from typing import List

class Solution:
    """
    A class used to represent the solution for finding the median of two sorted arrays.

    Methods
    -------
    findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float
        Returns the median of the two sorted arrays.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Returns the median of the two sorted arrays.

        Parameters
        ----------
        nums1 : List[int]
            The first sorted array.
        nums2 : List[int]
            The second sorted array.

        Returns
        -------
        float
            The median of the two sorted arrays.
        """
        # Combine the two arrays and find the median using the statistics module
        return statistics.median(nums1 + nums2)