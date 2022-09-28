/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode *now = head;
        int sz =1;
        while(now != nullptr){
            now = now->next;
            sz++;
        }
        
        int idx = sz-n-1;
        
        cout << idx;
        
        now = head;
        
        if(idx <= 0) {
            head = head->next;
            return head;
        };
        
        while(idx != 1){
            now = now->next;
            idx--;
        }
        
        now->next = now->next->next;
        
        
        return head;
    }
};