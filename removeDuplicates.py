#remove Dupliactes from sorted Array

def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    setList = set(nums)
    lst = list(setList)
    lst.sort()
    for i in range(len(lst)):
        nums[i] = lst[i]
    
    return len(lst)