class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # 模运算中可以多次取模，避免数字过大
        # 模运算的结果不会大于b，因此可以任意次数的再取模
        ans = 1
        
        while n!=0:
            
            if n%2 == 1:
                ans = (ans*a)%b
            
            a = a * a % b
            n //= 2
        return ans % b
