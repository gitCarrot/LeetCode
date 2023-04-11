class Solution:
    def removeStars(self, s: str) -> str:
        
        
        st = []
        
        for a in s:
            
            if a == '*' and st:
                st.pop()
            elif a != '*':
                st.append(a)
            
      
        
        
        return "".join(st)
            