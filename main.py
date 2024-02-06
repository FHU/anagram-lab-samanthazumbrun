
def anagram():
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

if __name__ == '__main__':
    word1 = input().lower().strip(' ')
    word2 = input().lower().strip(' ')
    print(anagram(word1, word2))


    