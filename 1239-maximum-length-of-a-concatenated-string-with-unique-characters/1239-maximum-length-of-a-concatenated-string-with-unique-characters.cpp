class Solution {
public:
    int maxlength = 0;
    void recur(vector<string>& arr, int pos, int length, int BIT){
        if(pos == arr.size()) {
            maxlength = max(maxlength, length); return;
        }
        recur(arr, pos +1, length, BIT);
        for(char c : arr[pos]) {
            if(1 << (c - 'a') & BIT) return;
            BIT |= 1 << (c - 'a');
        }
        recur(arr, pos +1, length + arr[pos].length() , BIT);
    }
    int maxLength(vector<string>& arr) {
        recur(arr, 0,0,0);
        return maxlength;
    }
};