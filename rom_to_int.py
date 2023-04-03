def romanToInt(s: str) -> int:
        romInt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
                  'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        integer = 0
        double = False #check if the two characters are in dictionary ex: IV 

        for i in range(1,len(s)):
            if double:  #skip next iteration
                double = False  
                continue
            if s[i-1] + s[i] in romInt:
                integer += romInt[s[i-1]+s[i]]
                double = True
            else:
                integer += romInt[s[i-1]]

        if not double:
            integer += romInt[s[-1]]
        return integer

#EX:
test1 = romanToInt('MCMXCIV')
test2 = romanToInt('LVIII')

print(test1)
print(test2)