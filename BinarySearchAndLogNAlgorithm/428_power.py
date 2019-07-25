import math
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        
        # 二分法来进行乘法计算
        if n == 0:
            return 1
        
        if n<0 and abs(x)>1:
            # 对于极大的负自然数n，若小于精确度则忽略之后的计算
            lowest_n_from_accuracy = int(-4/math.log10(x))-1
            if n<lowest_n_from_accuracy:
                return self.myPow(x, lowest_n_from_accuracy)
            else:
                return 1/self.myPow(x,-n)
        elif n<0:
            return 1/self.myPow(x, -n)

            
        if n%2 == 0:
            result = self.myPow(x, n//2)**2
        elif n%2 == 1:
            result = (self.myPow(x, (n-1)//2)**2)*x
            
        return result

    def real_efficient_myPow(self, x, n):
        # 快速幂
        if n < 0:
            x = 1/x
            n = -n
        ans = 1
        tmp = x


        while n != 0:
            if n%2 == 1:
                ans *= tmp
            tmp *= tmp
            n//=2
        return ans
