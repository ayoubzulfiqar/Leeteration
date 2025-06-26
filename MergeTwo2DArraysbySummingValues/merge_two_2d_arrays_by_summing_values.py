class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result = []
        p1 = 0
        p2 = 0
        n1 = len(nums1)
        n2 = len(nums2)

        while p1 < n1 and p2 < n2:
            id1, val1 = nums1[p1]
            id2, val2 = nums2[p2]

            if id1 == id2:
                result.append([id1, val1 + val2])
                p1 += 1
                p2 += 1
            elif id1 < id2:
                result.append([id1, val1])
                p1 += 1
            else:  # id1 > id2
                result.append([id2, val2])
                p2 += 1
        
        while p1 < n1:
            result.append(nums1[p1])
            p1 += 1
        
        while p2 < n2:
            result.append(nums2[p2])
            p2 += 1
            
        return result