import re
    
def palindrome(word):
    if type(word) == int:
        word = str(word)
    word = re.sub("[^a-zA-Z0-9]","", word).lower()
    if word == word[::-1]:
        return True
    else:
        return False




