bool isPalin(string str){
    int l = 0, r = str.length()-1;
    while(l <= r){
        if(str[l] != str[r]) return false;
        l++; r--;
    }
    return true;
}

class Solution {
    
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> mp;
        int total = 0, onePelin = 0, pel = 0;
        for(string word : words){
            bool isPal = isPalin(word); mp[word]++;
            if(isPal){
                if(mp[word] % 2 == 1) onePelin++;
                else --onePelin;
            }
            string temp = word;
            reverse(temp.begin(), temp.end());
            if(!isPal && mp[temp] >= mp[word]) total += 4;
            if(isPal && mp[temp] % 2 == 0) total += 4;
        }
        
        return total + (onePelin > 0 ? 2 : 0);
        
    }
};