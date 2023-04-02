#Find the index of the First occurance of string in other string
#return -1 if not found

def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1