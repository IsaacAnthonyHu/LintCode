class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        
        list_index = 0
        minimum_distance = 0
        default_list = []

        while True:
            minimum_distance = abs(target-A[list_index])
            list_index += 1
            if list_index > len(A)-1:
                default_list = A[-1-k:]
                break
            elif abs(target-A[list_index]) > minimum_distance:
                left_index = list_index-k
                right_index = list_index+k
                if left_index<0:
                    left_index = 0
                default_list = A[left_index: list_index+k]
                break
        
        distance_list = [(x,abs(x-target)) for x in default_list]
        sorted_list = sorted(distance_list, key=lambda x:x[1])
        target_list = [x[0] for x in sorted_list][:k]
        
        return target_list
