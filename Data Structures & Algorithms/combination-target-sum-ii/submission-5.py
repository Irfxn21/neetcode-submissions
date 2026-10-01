class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()
        def dfs(i, curr, total):
            if total == target and curr not in result:
                result.append(curr.copy())
                return
            if i>= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])

            h = curr.pop()
            j = i+1
            while j < len(candidates) and candidates[j]==h:
                j += 1
            dfs(j, curr, total)
        
        dfs(0,[],0)
        return result

        