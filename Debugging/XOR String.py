'''There Were 2 errors in this.The first one was assignment instead of comparission 
secondly the string was not getting added to the main string and instead was getting
assigned directly'''

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res


s = input()
t = input()
print(strings_xor(s, t))
