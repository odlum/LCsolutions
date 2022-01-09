# 42. Trapping Rain Water
# This solution worked for 317 of 320 tests. Timed out on 318 with very large input. Trying to rewrite it for increased efficiency.

class Solution:
    def trap(self, height: List[int]) -> int:
        
        s = 0
        j = len(height) - 1
        
        for z in range(0, max(height)):
            
            # print(height)
        
            i = 0
            while(height[i] == 0):
                i += 1
        
            while(height[j] == 0):
                j -= 1
        
            for x in range(i, j + 1):
                if(height[x] == 0):
                    s += 1
                else:
                    height[x] -= 1
                
                # print(i, j, x, s)
        
        return s
