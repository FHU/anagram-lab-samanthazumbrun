import main

def test_main():
    word1 = "yes"
    word2 = "no"

    assert main.anagram(word1, word2) == False