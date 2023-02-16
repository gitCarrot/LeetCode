class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        strnum = "".join(map(str, num))
        return list(map(int,str(int(strnum) + k)))
        
        