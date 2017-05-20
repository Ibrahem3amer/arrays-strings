class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        possible_length = len(needle)
        if possible_length < 1:
            return 0
        i = 0
        for char in haystack:
            if char == needle[0]:
                # Possible occurrence.
                if haystack[i:i+len(needle)] == needle:
                    return i
            i += 1  
        return -1
