import main

def test_main():
    word1 = "angel"
    word2 = "glean"

    assert main.anagram(word1, word2) == True