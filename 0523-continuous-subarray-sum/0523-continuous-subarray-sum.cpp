class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {   
        int len = nums.size();
        map<int,int> mods;
        int sum = 0, presum = 0;
        for(int n : nums){
            sum = (sum + n) % k;
            
            if(mods[sum]) return true;
            mods[presum]++;
            presum = sum;
        }
        return false;
    }
};