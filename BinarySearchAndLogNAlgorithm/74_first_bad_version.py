#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        
        head = 1
        tail = n
        
        while tail > head+1:
            
            mid = (head+tail)//2
            
            if SVNRepo.isBadVersion(mid):
                
                tail = mid
            
            else:
                
                head = mid
            
        if SVNRepo.isBadVersion(head):
            return head
        else:
            return tail
