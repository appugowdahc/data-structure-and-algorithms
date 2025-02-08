def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words

    # Early return if the total length of all words is greater than s
    if total_len > len(s):
        return []

    # Counter for the words
    word_count = Counter(words)
    
    # Resultant indices
    result_indices = []

    # Sliding window over the string s
    for i in range(word_len):
        left = i
        right = i
        current_count = Counter()
        
        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len
            
            if word in word_count:
                current_count[word] += 1
                
                while current_count[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    current_count[left_word] -= 1
                    left += word_len
                
                if right - left == total_len:
                    result_indices.append(left)
            else:
                current_count.clear()
                left = right

    return result_indices

# Example 1
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(findSubstring(s1, words1))  # Output: [0, 9]

# Example 2
s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(findSubstring(s2, words2))  # Output: []

s2 = "a"
words2 = ["a"]
print(findSubstring(s2, words2))  # Output: []



####################################
def findSubstring(s, words):
    if not s or not words or not words[0]:
        return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_count = {}
    
    # Initialize the word_count dictionary
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    result = []
    
    # Slide over the string in windows of size total_len
    for i in range(len(s) - total_len + 1):
        seen = {}
        for j in range(num_words):
            word_start = i + j * word_len
            word = s[word_start:word_start + word_len]
            
            if word in word_count:
                seen[word] = seen.get(word, 0) + 1
                # If a word is seen more times than it appears in words, break
                if seen[word] > word_count[word]:
                    break
            else:
                break
        else:
            # If we successfully checked all words, add the starting index
            result.append(i)
    
    return result

# Example usage
print(findSubstring("barfoothefoobarman", ["foo", "bar"]))  # Output: [0, 9]
print(findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  # Output: []



