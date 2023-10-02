def palindrome(word):
    if len(word) == 1:
        return True
    elif len(word) == 2:
        return word[0] == word[-1]
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return False
        
word = ('tacocat')
word1 = ('Malek')
print(palindrome(word))
print(palindrome(word1))
