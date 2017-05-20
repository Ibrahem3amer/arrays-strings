class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow_runner = 0
        fast_runner = 1
        if len(nums) >= 2:
            while(fast_runner < len(nums)):
                if nums[slow_runner] == nums[fast_runner]:
                    fast_runner += 1
                else:
                    slow_runner += 1
                    # Grapping the next greater number next to current number. Note that it's a sorted array.
                    nums[slow_runner] = nums[fast_runner]   
                    fast_runner += 1
        else:
            return len(nums)
                
        # + 1 because it's a zero-based pointer.                 
        return slow_runner + 1
