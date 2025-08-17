def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    frequency = [0] * 26  #26 letters in alphabet
    
    for letter in s:
        frequency[ord(letter) - ord('a')] += 1
    for letter in t:
        frequency[ord(letter) - ord('a')] -= 1
    
    for element in frequency:
        if element != 0:
            return False
    
    return True


print(isAnagram('racecar', 'caracre')) # True
print(isAnagram('car', 'rat')) # False
print(isAnagram('safe', 'asfr')) # False