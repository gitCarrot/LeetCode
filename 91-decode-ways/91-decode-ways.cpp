class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        if(n==0 || s[0]=='0') return 0;
        vector<int> f(n+1,0);
        f[0] = f[1] = 1;
        for(int i=2;i<=n;i++)
        {
            if(s[i-1]!='0') f[i] += f[i-1];
            if(s[i-2]=='1' || s[i-2]=='2' && s[i-1]<='6')
                f[i] += f[i-2];
        }
        return f[n];
    }
};