class Solution:
    """
    A class used to encapsulate the solution for finding the maximum number obtainable
    by swapping two digits of a given number.
    """

    def maximumSwap(self, num: int) -> int:
        """
        Find the maximum number obtainable by swapping two digits of the given number.

        Parameters
        ----------
        num : int
            The input number.

        Returns
        -------
        int
            The maximum number obtainable by swapping two digits.
        """
        # Convert the number to a list of digits
        digits = list(str(num))
        
        # Create a dictionary to store the last position of each digit (0-9)
        last = {int(d): i for i, d in enumerate(digits)}
        
        # Traverse the digits
        for i, d in enumerate(digits):
            # Check if there exists a larger digit later in the number
            for larger in range(9, int(d), -1):
                if last.get(larger, -1) > i:
                    # Perform the swap
                    digits[i], digits[last[larger]] = digits[last[larger]], digits[i]
                    # Return the result as an integer
                    return int(''.join(digits))
        
        # If no swap is performed, return the original number
        return num