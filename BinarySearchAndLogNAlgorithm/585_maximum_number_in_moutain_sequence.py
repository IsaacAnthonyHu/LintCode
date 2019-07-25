
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        index = 0
        try:
            while nums[index] <= nums[index+1]:
                index += 1
            return nums[index]
        except IndexError:
            return nums[index]
