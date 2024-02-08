def anagram(word1, word2):
    word1 = word1.lower().replace(" ","")
    word2 = word2.lower().replace(" ","")
    if word1.isspace():
        return False
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

if __name__ == '__main__':
    word1 = input()
    word2 = input()
    print(anagram(word1, word2))
    #test


    