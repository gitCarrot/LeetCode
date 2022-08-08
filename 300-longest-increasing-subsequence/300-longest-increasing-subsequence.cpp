class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
    vector<int> v;
        
    v.push_back(-10001);

    for(int i = 0; i<nums.size(); i++){
        
        if(v.back() >= nums[i]){
            auto it = lower_bound(v.begin(), v.end(), nums[i]);
            *it = nums[i];
        }else{
            v.push_back(nums[i]);
        }


    }

    return v.size()-1; 
        
        
        
    }
};