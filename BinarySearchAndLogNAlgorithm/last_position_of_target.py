class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        
        if not nums or target is None:
            return -1
        
        head_index = 0
        tail_index = len(nums)-1
        
        while tail_index > head_index+1:
            # 最终缩小为两个数情况时的判定
            
            mid_index = (head_index + tail_index)//2
            
            if nums[mid_index] > target:
                tail_index = mid_index
            elif nums[mid_index] < target:
                head_index = mid_index
            else:
                # 若中间数等于目标数，我们要的是最后一个目标数的index，
                # 所以取尾不取头，取后半段，也即[mid, tail]
                head_index = mid_index
        
        if nums[tail_index] == target:
            return tail_index
        elif nums[head_index] == target:
            return head_index
        else:
            return -1
        
        
            
