'''
pseudo:
    
    what do i know:
        - anagram is a word/phrase formed by morphing letters into a new word
            (i.e cat -> tac)

    
    what do i need to do:
        - compare s and t, respectively
'''

def isAnagram(s,t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

print(isAnagram("anagram", "nagaram"))
print(isAnagram("anagram", "nagaramf"))
