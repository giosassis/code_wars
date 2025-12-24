def highest_scoring_word(text: str) -> str:
    words = text.split()
    score = 0
    for word in words:
        word_score = 0
        for letter in word:
            word_score += ord(letter) - 96
        if word_score > score:
            score = word_score
            highest_word = word
    return highest_word

print(highest_scoring_word("man i need a taxi up to ubud"))
print(highest_scoring_word("what time are we climbing up the volcano"))
print(highest_scoring_word("take me to semynak"))

