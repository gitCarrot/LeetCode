class Solution {
public:
    int maxlength = 0;
    
    void recur(vector<string>& arr, int pos, int length, int BIT){
        if(pos == arr.size()) {
            maxlength = max(maxlength, length);
            return;
        }
        recur(arr, pos +1, length, BIT);
        
        string curstring = arr[pos];
        for(char c : curstring) {
            if(1 << (c - 'a') & BIT) return;
            else BIT |= 1 << (c - 'a');
        }
        length += curstring.length();
        recur(arr, pos +1, length , BIT);
    }
    int maxLength(vector<string>& arr) {
        recur(arr, 0,0,0);
        return maxlength;
    }
};