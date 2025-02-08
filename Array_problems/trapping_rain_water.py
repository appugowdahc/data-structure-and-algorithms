class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                right -= 1
        
        return water_trapped



class Solution1:
    def trap(self, height) -> int:
        arr = height
        if not height:
            return
        
        res = 0
        left_max_arr = [0]
        right_max_arr = [0]*len(height)
        lmax = arr[0]
        rmax = arr[-1]

        l = len(height)
        for i in range(1,l):
            left_max_arr.append(lmax)
            lmax = max(lmax,arr[i])

        for j in range(l-2,-1,-1):

            right_max_arr[j]=rmax
            rmax = max(rmax,arr[j])
        
        for i in range(l):
            min_height = min(left_max_arr[i],right_max_arr[i])
            total_water = min_height - arr[i]
            if total_water >0:
                res+= total_water
        return res

s = Solution1()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))