def anagram(word1, word2):
    pass

if __name__ == '__main__':
    word1 = input("Enter word 1: ")
    word2 = input("Etner word 2: ")
    result = anagram(word1, word2)


#ben and hannah = False

#Solution
'''def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    
    word1 = word1.replace(" ","")
    word2 = word2.replace(" ","")
    
    if len(word1) == 0 or len(word2) == 0:
        return False
    elif len(word1) != len(word2):
        return False
    else:
        srt1 = list(word1)
        srt2 = list(word2)
        
        srt1.sort()
        srt2.sort()
        
        for i in range(len(srt1)):
            if srt1[i] == srt2[i]:
                continue
            else:
                return False
        return True

word1 = input("Enter word 1: ")
word2 = input("Etner word 2: ")

result = anagram(word1, word2)

print(result)'''