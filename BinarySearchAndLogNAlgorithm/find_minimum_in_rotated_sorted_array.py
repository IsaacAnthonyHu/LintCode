class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        
        length = len(nums)
        
        for x in range(length):
            
            left_index = x-1
            right_index = x+1
            
            if left_index < 0:
                left_index = 0
            
            if right_index >= length:
                right_index = length-1
            
            if nums[left_index] > nums[x] and nums[x] < nums[right_index]:
                return nums[x]
                
                
        return min(nums[0], nums[-1])
