# Steps:
# 1) create empty dictionary
# 	- key: numbers/values in the list provided
# 	- value: number of occurrences
# 2) loop over list, increment values of list# keys (ex: 3 seen in list, increment dictionary with key 3 by one)
# 3) sort dictionary by **KEYS ** (the actual NUMBERS), greatest to least
# 4) create empty result list
# 5) loop over dictionary k times
# 	- store each number/occurrence pair in num/count
# 	- append the NUM to the result list
# 6) return the result
# -------------------------------------------------------------------------
# Total: O(n + m log m) time, O(m) space
# not optimal, but good enough

def topKFrequent(nums, k):
    frequency = {} # empty dictionary

    # count frequencies in dictionary
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # sorted dictionary of (key, value) pairs (greatest to least)
    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    result = [] # result list (will store the most frequent values)

    # take the k highest values
    for i in range(k):
        num, count = sorted_items[i] # stores the key in num, value in count, for the sorted dictionary at index i
        result.append(num)  # add values to list
    
    return result # return / print

print(topKFrequent([1,2,2,3,3,3], 2))
print(topKFrequent([7,7], 1))