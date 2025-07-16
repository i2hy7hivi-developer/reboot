check_anagram = input("Enter two words separated by a space to check if they're anagrams: ").strip().lower()
word1, word2 = check_anagram.split()

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    
    char_count = {}
    
    # Count characters in the first word
    for char in word1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract character counts using the second word
    for char in word2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True

if is_anagram(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")