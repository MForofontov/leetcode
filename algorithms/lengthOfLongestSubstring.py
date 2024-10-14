class Solution:
    """
    A class used to represent the solution for finding the length of the longest substring without repeating characters.

    Methods
    -------
    lengthOfLongestSubstring(s: str) -> int
        Returns the length of the longest substring without repeating characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring without repeating characters.

        Parameters
        ----------
        s : str
            The input string.

        Returns
        -------
        int
            The length of the longest substring without repeating characters.
        """
        char_index_map = {}  # To store the last index of each character
        max_length = 0
        start = 0  # Start pointer for the sliding window

        for end in range(len(s)):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                # If the character is already in the map and its index is within the current window
                start = char_index_map[s[end]] + 1  # Move the start pointer to the right of the last occurrence

            char_index_map[s[end]] = end  # Update the last index of the character
            max_length = max(max_length, end - start + 1)  # Update max length

        return max_length