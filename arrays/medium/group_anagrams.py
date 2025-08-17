from typing import List
from collections import defaultdict

# Solution #1
def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    buckets = {}  # key: 26-tuple signature, value: list of words

    for i in range(len(strs)): # for each word in the list
        count = [0] * 26 # declare an empty alpha list
        for ch in strs[i]: # loop through every character
            count[ord(ch) - ord('a')] += 1  # assumes lowercase a–z -> increase each letter's corresponding cell by 1
        
        key = tuple(count) # makes list immutable (converted to tuple)

        if key not in buckets: # checks dictionary KEYS
            buckets[key] = [] # key is the tuple/list of 1s and 0s -> create empty list for words represented by that tuple
        buckets[key].append(strs[i]) # append current word

    return list(buckets.values())

# Explanation:
# - empty dictionary declared
# - loop over each word in list
# - loop over each character, create a 26-cell list representing letters in each word
# - convert list to tuple (IMMUTABLE)
# - if character array is NOT in the dictionary, create an empty list element under that KEY
# - Ex: if char key of (1T, 1E, 1A) doesn't have its own sublist yet, CREATE ONE!
# - once key exists, append current word to its key sublist
# - return dictionary values in list form

# Time Complexity: O(m*n) -> 'm' loops over each word, 'n' loops over each letter


# Solution #2
def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
    
        res[tuple(count)].append(s)
    
    return list(res.values())

# Explanation:
# - empty dictionary declared (defaulted to an empty list)
# - loop over each word (s) in list
# - declare character list for each word (count number of each letter in string)
# - loop through each character (c) in word (s)
# - increment corresponding letter values in list
# - converts key to tuple and appends word to that key automatically - defaultdict creates empty list if key doesn't exist yet
# - return dictionary in list form

# Time Complexity: O(m*n) -> 'm' loops over each word, 'n' loops over each letter

print(groupAnagrams1(["act","pots","tops","cat","stop","hat"]))
print(groupAnagrams1(["x"]))

print(groupAnagrams2(["act","pots","tops","cat","stop","hat"]))
print(groupAnagrams2(["x"]))