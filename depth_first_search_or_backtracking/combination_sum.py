class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def depth_first_search(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            depth_first_search(i,curr,total+candidates[i])
            curr.pop()
            depth_first_search(i+1,curr,total)

        depth_first_search(0,[],0)
        return res
        
        
#####################################
def combinationSum(candidates, target):
    result = []
    
    def backtrack(remain, combo, start):
        if remain == 0:
            # If we have hit the target, add the current combination to the result
            result.append(list(combo))
            return
        elif remain < 0:
            # If the remaining sum is negative, stop exploring further
            return
        
        for i in range(start, len(candidates)):
            # Include the current candidate and explore further
            combo.append(candidates[i])
            # Not incrementing i since the same element can be reused
            backtrack(remain - candidates[i], combo, i)
            # Backtrack by removing the last added element
            combo.pop()
    
    backtrack(target, [], 0)
    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))  # Output: [[2, 2, 3], [7]]
