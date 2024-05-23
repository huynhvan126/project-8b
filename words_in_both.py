# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/22/2024
# Description: Splits both input strings into lists of words, converts them to lowercase.
def words_in_both(str1, str2):
    """Convert both strings and split them into lists of common words."""
    words1 = str1.lower().split()
    words2 = str2.lower().split()
    common_words = set()
    for word in words1:
        if word in words2:
            common_words.add(word)
    return common_words