import main

def test_main():
    word1 = "Ben"
    word2 = "Hannah"

    assert main.anagram(word1, word2) == False