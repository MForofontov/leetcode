class Solution:
    """
    A class used to encapsulate the solution for calculating the minimum number of swaps
    required to group all black balls ('0') together in a given string.
    """

    def minimumSteps(self, s: str) -> int:
        """
        Calculate the minimum number of swaps required to group all black balls ('0') together.

        :param s: A string consisting of '0's (black balls) and '1's (white balls)
        :type s: str
        :return: The minimum number of swaps required
        :rtype: int
        """
        # Initialize variables
        black_count = 0  # Count of black balls encountered
        swaps = 0  # Total number of swaps required

        # Iterate over each character in the string
        for i in range(len(s)):
            if s[i] == '0':
                # Current index should be where the black ball can be placed
                swaps += i - black_count
                black_count += 1

        return swaps