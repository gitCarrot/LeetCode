class Solution {
public:
    int maxlength = 0;
    int maxLength(vector<string>& arr) {
        function<void(int,int,int)> recur = [&](int p, int l, int BIT) -> void {
            if(p == arr.size()) {
                maxlength = max(maxlength, l); return;
            }
            recur(p +1, l, BIT);
            for(char c : arr[p]) {
                if(1 << (c - 'a') & BIT) return;
                BIT |= 1 << (c - 'a');
            }
            recur(p +1, l + arr[p].length() , BIT);
        };
        recur(0,0,0);
        return maxlength;
    }
};