class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popidx = 0
        st = []
        for i in pushed:
            st.append(i)
            while len(st) != 0 and popped[popidx] == st[-1]:
                st.pop()
                popidx += 1
                
        if len(st) > 0:
            return False
        else:
            return True
            
            
            
        