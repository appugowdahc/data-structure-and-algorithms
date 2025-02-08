
def combinationSum2(candidates, target):
    candidates.sort()  # Sort to handle duplicates easily
    res = []

    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        if i >= len(candidates) or total > target:
            return

        # Include the current candidate
        curr.append(candidates[i])
        dfs(i + 1, curr, total + candidates[i])
        curr.pop()

        # Skip duplicates by advancing the index to the next distinct candidate
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1

        # Exclude the current candidate and move to the next
        dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return res
    
arr = [10,1,2,7,6,1,5]
t= 8
combinationSum2(arr,8)
    
    #################################
def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # If the current number is greater than the remaining target, no need to proceed further
            if candidates[i] > target:
                break
            # Include the current number and move to the next one
            backtrack(i + 1, target - candidates[i], path + [candidates[i]])

    candidates.sort()
    res = []
    backtrack(0, target, [])
    return res
