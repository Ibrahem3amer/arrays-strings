class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        
        >>>twoSum([2,3,4], 6)
        [1, 3]
        >>>twoSum([2,4,5,8,9,12], 13)
        [3, 4]
        >>>twoSum([0,0,0,0], 0)
        [1, 4]
        >>>twoSum([0,0,1,1,2,2], 0)
        [1, 2]
        >>>twoSum([0,0,3,4], 0)
        [1, 2]
        """
        e_pointer   = len(numbers)-1
        b_pointer   = 0
        result = [b_pointer+1, e_pointer+1]
        while b_pointer < e_pointer:
            two_sum = numbers[b_pointer] + numbers[e_pointer]
            if two_sum == target:
                return [b_pointer+1, e_pointer+1]
            # We need a smaller sum, so we decrease the maximum number wich is e_pointer.
            elif two_sum > target:
                e_pointer -= 1
            else:
                b_pointer += 1
        return [-1, -1]
