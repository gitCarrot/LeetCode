class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        int mod = 1e9+7;
        int ans = 0;
        unordered_map<int,int> m;
        
        sort(arr.begin(), arr.end());
        
        
        for(int head = 0; head<arr.size(); head++){
            m[arr[head]] = 1;
                
            for(auto [c1, b] : m){
                if(arr[head] % c1 != 0) continue;
                
                int c2 = arr[head] / c1;
                if( c2 * c1 == arr[head] && m.find(c2) != m.end()){
                    m[arr[head]] =  (m[arr[head]] + (long)(m[c1]) * (long)(m[c2]) %mod) % mod;
                }       
            }
        }
        
        
        for(auto [head, value] : m){
            ans = (ans + value) % mod;
        }
        
        
        return ans;
    }
};