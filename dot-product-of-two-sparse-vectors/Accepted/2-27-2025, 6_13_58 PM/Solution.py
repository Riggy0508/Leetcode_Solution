// https://leetcode.com/problems/dot-product-of-two-sparse-vectors

class SparseVector:
    def __init__(self, nums: List[int]):
        self.hash1={}

        for i,val in enumerate(nums):
            if val!=0:
                self.hash1[i]=val


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result=0

        for i,val in self.hash1.items():
            if i in vec.hash1:
                result+=val*vec.hash1[i]

        return result

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)