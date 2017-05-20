class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        >>>isAnagram("anagram","nagaram")
        True
        >>>isAnagram("car","rat")
        False
        """
        dic = {}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        for char in t:
            if char in dic and dic[char] >= 1:
                dic[char] -= 1
            else:
                return False
        if sum(dic.values()) == 0:
            return True
        else:
            return False
