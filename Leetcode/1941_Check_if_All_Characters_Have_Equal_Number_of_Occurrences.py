class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        ans = True
        p = next(iter((d.items())) )
        n = p[1]

        

        for i in d:
            if d[i]!=n:
                return False
                break
        return True
        
