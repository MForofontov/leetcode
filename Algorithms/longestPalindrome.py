class Solution:
    """
    A class used to represent the solution for finding the longest palindromic substring.

    Methods
    -------
    longestPalindrome(s: str) -> str
        Returns the longest palindromic substring in the given string.
    """
    def longestPalindrome(self, s: str) -> str:
        """
        Returns the longest palindromic substring in the given string.

        Parameters
        ----------
        s : str
            The input string.

        Returns
        -------
        str
            The longest palindromic substring.
        """
        if not s or len(s) == 0:
            return ""

        def expandAroundCenter(left: int, right: int) -> str:
            """
            Expands around the center and returns the longest palindrome substring.

            Parameters
            ----------
            left : int
                The left index to start expansion.
            right : int
                The right index to start expansion.

            Returns
            -------
            str
                The longest palindrome substring found by expanding around the center.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""
        for i in range(len(s)):
            # Check for odd-length palindromes (single character as center)
            odd_palindrome = expandAroundCenter(i, i)
            # Check for even-length palindromes (two characters as center)
            even_palindrome = expandAroundCenter(i, i + 1)

            # Update longest palindrome found
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)

        return longest_palindrome