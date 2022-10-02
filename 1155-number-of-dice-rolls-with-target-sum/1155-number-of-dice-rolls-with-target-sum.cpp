class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        
        
        long long dp[31][1001] = {0,};
        
        dp[1][1] = 1;
        
        
        for(int dice = 1; dice <= k; dice++){
            dp[1][dice] = 1;
        }
       
        
        
        for(int i = 2; i<=n; i++){
            for(int j = i; j<=target; j++){
                if(i == j) {
                    dp[i][j] = 1;  
                    continue;
                }
                long long add = 0;
                for(int dice = 1; dice <= k; dice++){
                    if(j-dice >= 1){
                        add += dp[i-1][j-dice];
                    }
                }                
                dp[i][j] += (add) % 1000000007;
            }
        }
        
        
        return (int)dp[n][target] % 1000000007;
        
    }
};