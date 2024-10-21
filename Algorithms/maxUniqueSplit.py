class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, current_set):
            # Base case: if we have gone through the entire string
            if start == len(s):
                return len(current_set)
            
            # Variable to store the maximum number of unique substrings
            max_splits = 0
            
            # Try to split the string starting from 'start' index
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # If the substring is not already in the set, we can choose it
                if substring not in current_set:
                    current_set.add(substring)
                    # Continue backtracking with the remaining string
                    max_splits = max(max_splits, backtrack(end, current_set))
                    # Remove the substring after exploring this path (backtrack)
                    current_set.remove(substring)
            
            return max_splits
        
        # Start backtracking from index 0 with an empty set of unique substrings
        return backtrack(0, set())
