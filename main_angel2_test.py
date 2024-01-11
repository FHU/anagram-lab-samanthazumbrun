import main

def test_main():
    word1 = "An geL"
    word2 = "glE an"

    assert main.anagram(word1, word2) == True