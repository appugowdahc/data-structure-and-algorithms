"""
506. Relative Ranks
Easy
Topics
Companies
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].


"""
from typing import List


######### optimal solution

import copy
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        #copy score array with deep copy to make sure it should not affect
        #original array
        score1 = copy.deepcopy(score)
        
        #to get heighest score in score
        score1.sort(reverse=True)
        res = ["Gold Medal","Silver Medal","Bronze Medal"]
        #where each score will hold rank
        rank_dict = {}
        for idx,scr in enumerate(score1):
            if idx <=2: 
                rank_dict[scr] = res[idx]
            else:
                rank_dict[scr] = str(idx+1)
        

        for i in range(len(score)):
            score[i] = rank_dict[score[i]]
        return score

########### brute force approach

import copy
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ranks = [""] * n  # Store ranks
        sorted_scores = sorted(score, reverse=True)  # Sort in descending order

        for i in range(n):
            # this approach will be O(n**2) because iteration and index look up
            rank = sorted_scores.index(score[i]) + 1  # Find position in sorted list
            if rank == 1:
                ranks[i] = "Gold Medal"
            elif rank == 2:
                ranks[i] = "Silver Medal"
            elif rank == 3:
                ranks[i] = "Bronze Medal"
            else:
                ranks[i] = str(rank)
        
        return ranks
