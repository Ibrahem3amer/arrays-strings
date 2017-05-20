class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if not str:
            return 0
        sum_var = []
        expections = ['+', '-', ' ']
        exception_flag = False
        negative_flag = False
        integeral_flag = False
        for char in str:
            if 48 <= ord(char) <= 57:
                num = self.to_num(ord(char))
                sum_var.append(num)
                integeral_flag = True
            elif char in expections and not exception_flag and not integeral_flag:
                exception_flag = True if char != ' ' else False
                negative_flag = True if char == '-' else False
                continue
            else:
                break
        max_base = 10 ** (len(sum_var)-1)
        sum_int = 0
        for num in sum_var:
            sum_int += abs(max_base * num)
            max_base /= 10
    
        
        sum_int = sum_int * -1 if negative_flag else sum_int
        if len(sum_var) < 1:
            return 0
        elif sum_int > INT_MAX:
            sum_int =  INT_MAX
        elif sum_int < INT_MIN:
            sum_int =  INT_MIN
        return sum_int
        
    def to_num(self, char_ord):
        return char_ord - 48
