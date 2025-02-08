
from collections import defaultdict, deque

words = ["wrt", "wrf", "er", "ett", "rftt"]


def find_order(words):
    in_degree = defaultdict(set)
    adj_list = defaultdict(set)
    
    for word in words:
        for char in word:
            in_degree[char] = 0
            
    for i in range(len(words)-1):
        first_word = words[i]
        second_word = words[i+1]
        
        min_length  = min(len(first_word),min(second_word))
        
        # Check for prefix case (invalid order)
        if len(first_word) > len(second_word) and first_word[:min_length] == second_word[:min_length]:
            return ""  # Invalid case
        
        for j in range(min_length):
            
            if first_word[j] != second_word[j]:
                if 
    
    