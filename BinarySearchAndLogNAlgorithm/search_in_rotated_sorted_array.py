class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        
        if not A:
            return -1
        
        head = 0
        tail = len(A)-1
        
        while tail>head+1:
            
            mid = (head+tail)//2
            
            if (A[mid]<A[tail] and target>A[tail]) or (A[mid]<A[tail] and target<=A[mid]):
                
                tail = mid
            
            elif A[mid]<A[tail]:
                
                head = mid
            
            elif (A[mid]>A[tail] and target>A[mid]) or (A[mid]>A[tail] and target<=A[head]):
                
                head = mid
            
            elif A[mid]>A[tail]:
                
                tail = mid
        
        if A[head] == target:
            return head
        elif A[tail] == target:
            return tail
        else:
            return -1
