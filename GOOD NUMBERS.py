class Solution(object):
    def countGoodNumbers(self, n):
        MOD=10**9+7
        def expo(x,n):
            if (n==0):
                return 1
            elif(n&1==0):
                return expo(x**2 %MOD,n//2)
            return (x*expo(x,n-1))% MOD
        return 5**(n%2) * expo(20,n//2)%MOD
             
        """
        :type n: int
        :rtype: int
        """

        