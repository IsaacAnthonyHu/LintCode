class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        
        
        
        head = 1
        tail = len(A)-2
        
        while tail > head+1:
            
            mid = (head+tail)//2 
            
            if A[mid] < A[mid-1]:
                
                tail = mid
            elif A[mid] < A[mid+1]:
                
                head = mid
            else:
                head = mid
            
        if A[head]>A[tail]:
            return head
        else:
            return tail
