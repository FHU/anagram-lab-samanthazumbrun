import main

def test_main():
    word1 = "Ra il Safety"
    word2 = "fairy tales"

    assert main.anagram(word1, word2) == True