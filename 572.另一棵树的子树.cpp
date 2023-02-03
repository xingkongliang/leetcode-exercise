/*
 * @lc app=leetcode.cn id=572 lang=cpp
 *
 * [572] 另一棵树的子树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSametree(TreeNode *s, TreeNode *t)
    {
        if (s == NULL && t == NULL) return true;
        return s && t 
            && s->val == t->val
            && isSametree(s->left, t->left)
            && isSametree(s->right, t->right);
    };
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (s == NULL && t == NULL) return true;
        if (s == NULL && t != NULL) return false;
        return isSametree(s, t) 
            || isSubtree(s->left, t)
            || isSubtree(s->right, t);
    }
};
// @lc code=end

