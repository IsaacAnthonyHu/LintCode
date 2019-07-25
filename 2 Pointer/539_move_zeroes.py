def movezeroes(nums):

    length = len(nums)
    nonzero_index = 0
    list_index = 0

    while list_index < length-1:
        if nums[list_index] == 0:
            nonzero_index = list_index
            while nonzero_index < length-1 and nums[nonzero_index] == 0:
                nonzero_index += 1
            nums[list_index], nums[nonzero_index] = nums[nonzero_index], nums[list_index]
        list_index += 1
        print(nums)
    return nums

def movezeroes_fast(nums):
    left, right = 0, 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

def movezeroes_self(nums):
    left, right = 0, 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

def movezeroes_pythonic(nums):

    i=0
    for num in nums:
        if num != 0:
            num[i] = num
            i += 1
    for j in range(i, len(nums)):
        nums[j] = 0
    return nums
