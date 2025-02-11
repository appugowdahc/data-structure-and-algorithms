"""
495. Teemo Attacking
Solved
Easy
Topics
Companies
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

 

Example 1:

Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
Example 2:

Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
    
"""
from typing import List
###########brute force
def findPoisonedDurationBruteForce(timeSeries, duration):
    poisoned_time = set()
    
    for t in timeSeries:
        for sec in range(t, t + duration):
            poisoned_time.add(sec)  # Store poisoned seconds

    return len(poisoned_time)

# Test Cases
print(findPoisonedDurationBruteForce([1,4], 2))  # Output: 4
print(findPoisonedDurationBruteForce([1,2], 2))  # Output: 3


############ my solution
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        res += duration

        for i in range(1,len(timeSeries)):
            val = timeSeries[i] - timeSeries[i-1]

            if val < duration:
                res -= duration -val
            res += duration
        return res
        

############optimal solution 

def findPoisonedDurationOptimal(timeSeries, duration):
    if not timeSeries:
        return 0  # No attacks

    total_time = 0

    for i in range(len(timeSeries) - 1):
        total_time += min(duration, timeSeries[i + 1] - timeSeries[i])  # Add non-overlapping duration

    return total_time + duration  # Add duration for the last attack

# Test Cases
print(findPoisonedDurationOptimal([1,4], 2))  # Output: 4
print(findPoisonedDurationOptimal([1,2], 2))  # Output: 3
