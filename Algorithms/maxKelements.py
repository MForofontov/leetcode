import heapq
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        """
        Returns the maximum score by selecting k elements from the list. Each selected element is divided by 3 (rounded up) and pushed back into the list.

        Parameters
        ----------
        nums : List[int]
            List of integers.
        k : int
            Number of elements to select.

        Returns
        -------
        int
            The maximum score obtained by selecting k elements.
        """
        # Create a max-heap by inserting negative values
        max_heap = [-num for num in nums]  # Store negative to simulate a max-heap
        heapq.heapify(max_heap)  # Transform the list into a heap in-place
        
        score = 0

        for _ in range(k):
            # Pop the largest value (remember it's negative, so we negate it)
            max_val = -heapq.heappop(max_heap)
            score += max_val  # Increase score by the maximum value
            
            # Calculate the new value and push it back to the heap
            new_val = (max_val + 2) // 3  # Use integer division for better performance
            heapq.heappush(max_heap, -new_val)  # Push the new value back as negative

        return score