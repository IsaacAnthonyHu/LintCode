# For a given source string an a target string, you should ouput the first index(from 0) of target string in sourc string.
# If target does not exist in source, just return -1.
# KMP Algorithm?

#Example 1:
#Input: source = "source", target = "target"
#Output: -1

#Example 2:
#Input: source = "abcdabcdefg", target = "bcd"
#Output: 1


def str(source, target):

    if target == "":
        return 0
    
    for x in range(len(source)):
        target_index = 0
        source_index = x
        if source[x] == target[target_index]:
            while source[source_index] == target[target_index]:
                if target_index+1 == len(target):
                    return x
                source_index += 1
                target_index += 1
                if source_index+1 > len(source):
                    return -1
                    
    return -1
