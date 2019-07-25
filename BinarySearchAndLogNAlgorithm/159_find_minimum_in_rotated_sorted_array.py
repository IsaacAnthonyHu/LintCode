class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        
        if not nums:
            return -1
        
        head_index = 0
        tail_index = len(nums)-1

        while tail_index > head_index + 1:
            
            mid_index = (head_index+tail_index)//2
            
            if nums[mid_index] > nums[tail_index]:
                head_index = mid_index
                
            else:
                tail_index = mid_index
            
        return min(nums[head_index], nums[tail_index])
