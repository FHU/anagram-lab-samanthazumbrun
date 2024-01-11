import main

def test_main():
    word1 = "rail safety"
    word2 = "fairy tales"

    assert main.anagram(word1, word2) == True