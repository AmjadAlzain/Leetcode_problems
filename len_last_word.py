def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    #convert to list of words
    lst = s.split()

    #return length of item in list
    return len(lst[-1])

#Ex

test = "Count the length of last word"
print(lengthOfLastWord(test))   #return 4
        