class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = []
        results = [0]
        # Sliding window concept. 
        i, j, n = 0, 0, len(s)
        while(i < n and j < n):
            if(s[j] in substring):
                i += 1
                results.append(len(substring))
                substring = []
            else:
                substring.append(s[j])
                j += 1
        return max(results)
