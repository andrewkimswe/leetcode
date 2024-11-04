class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        
        reversed_num = 0
        while x_abs != 0:
            reversed_num = reversed_num * 10 + x_abs % 10
            x_abs //= 10
        
        reversed_num *= sign
        
        # 32비트 정수 범위 내인지 확인
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        return reversed_num
