class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        
        
        int score = 0;
        int mx = 0;
        
        sort(tokens.begin(), tokens.end());
        if(tokens.size() == 0 || power < tokens[0]) return 0;
        int l = 0, r = tokens.size()-1;
        
        while(l<=r){
            
            if(power - tokens[l] >=0){
                power -= tokens[l++];
                score++;
            }else{
                power += tokens[r--];
                score--;
            }
            
            mx = max(mx, score);
            
        }
        
        return mx;
        
    }
        
        
        
        
    
};