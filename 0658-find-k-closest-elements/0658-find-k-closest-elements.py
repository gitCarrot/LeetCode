class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def lb(arr, x):
            l, r = 0, len(arr)-1
            ans = len(arr)
            while l<=r:
                mid = (l+r)//2
                if arr[mid] >= x:
                    ans = mid
                    r = mid -1
                else:
                    l = mid + 1
                    
            return ans
                 
                
        idx = lb(arr, x)
        if idx == len(arr): idx -= 1
        elif idx >= 1 and arr[idx] - x >= x - arr[idx-1]:
            idx -= 1

        anslist = []
        
        k -= 1
        anslist.append(arr[idx])
        
        lidx, ridx = idx -1, idx + 1
        while k:
            k-=1
            if lidx < 0: 
                anslist.append(arr[ridx])
                ridx += 1
            elif ridx >= len(arr):
                anslist.append(arr[lidx])
                lidx -= 1
            else:
                if x - arr[lidx] <= arr[ridx] - x:
                    anslist.append(arr[lidx])
                    lidx -= 1
                elif x - arr[lidx] > arr[ridx] - x:
                    anslist.append(arr[ridx])
                    ridx += 1
                    
        
            
                    
        return sorted(anslist)
        
        
        
            
        