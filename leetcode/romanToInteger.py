'''

'''

class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        length=len(s)
        for i in s:
            total+=dict1[i]
        s=s[-1:-len(s)-1:-1]
        for k in range(0,len(s)-1):
           if dict1[s[k]]>dict1[s[k+1]]:
             total-=2*(dict1[s[k+1]])
           else:
             continue
        return total