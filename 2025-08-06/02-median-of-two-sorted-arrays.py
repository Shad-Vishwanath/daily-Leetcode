"""🔗 LeetCode Link: Median of Two Sorted Arrays

🧠 Problem Summary:
Given two sorted arrays nums1 and nums2, return the median of the two sorted arrays.

Must run in O(log(min(n, m))) time — but this implementation uses a simple linear merge approach.

✅ Solution Status:
✔️ Accepted – Passed all 2097 test cases
⚡ Runtime: 7 ms (Beats 29.69% of submissions)
💾 Memory: 12.51 MB (Beats 77.25%)

💡 Approach:
Performed a linear merge similar to merge sort to find the middle elements directly.

Tracked two pointers i and j for nums1 and nums2.

Found the median by iterating until we reached the middle of the merged array.

This solution does not use the optimal O(log(min(n, m))) approach, but it is clean, intuitive, and accepted for all test cases.

🧪 Complexity:
Time Complexity: O((n + m)/2)

Space Complexity: O(1) – no extra memory used
"""
Program :
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0

        # Find median.
        for count in range(0, (n + m) // 2 + 1):
            m2 = m1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < n:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1

        # Check if the sum of n and m is odd.
        if (n + m) % 2 == 1:
            return float(m1)
        else:
            ans = float(m1) + float(m2)
            return ans / 2.0
        
