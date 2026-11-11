class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
            d={}
            for i in arr:
                if i not in d:
                    key=i
                    value=arr.count(i)
                    d[key]=value
            s1=len(set(d.values()))
            s2=len(d.values())
            if s1==s2:
                return True
            else:
                return False
        