def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: output: List[int]
    """
    output = []
    flag = False
    for ip, i in enumerate(nums):
        if flag:
            break
        for jp, j in enumerate(nums):
            if ip == jp:
                continue
            if (i+j) == target:
                output.append(ip)
                output.append(jp)
                flag = True
                break
    return output
