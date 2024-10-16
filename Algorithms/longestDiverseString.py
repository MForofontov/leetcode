import heapq
from typing import List, Tuple

class Solution:
    """
    A class used to generate the longest possible diverse string containing 'a', 'b', and 'c'
    such that no three consecutive characters are the same.
    """

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Generate the longest possible diverse string containing 'a', 'b', and 'c'
        such that no three consecutive characters are the same.

        Parameters
        ----------
        a : int
            The number of 'a' characters available.
        b : int
            The number of 'b' characters available.
        c : int
            The number of 'c' characters available.

        Returns
        -------
        str
            The longest possible diverse string.
        """
        # Create a max-heap based on the counts of a, b, and c
        max_heap: List[Tuple[int, str]] = []
        
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        
        result: List[str] = []
        
        while max_heap:
            # Get the character with the highest count
            count1, char1 = heapq.heappop(max_heap)
            # If the last two characters in the result are the same as the current character, use the second most frequent
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not max_heap:
                    break  # No other characters to choose from, so we are done
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)
                count2 += 1  # Decrement its count (since it's negative in the heap)
                if count2 < 0:
                    heapq.heappush(max_heap, (count2, char2))
                # Push back the first character into the heap
                heapq.heappush(max_heap, (count1, char1))
            else:
                result.append(char1)
                count1 += 1  # Decrement its count (since it's negative in the heap)
                if count1 < 0:
                    heapq.heappush(max_heap, (count1, char1))
        
        return ''.join(result)