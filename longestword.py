def longestWord(word):
    max_length = len(word[0])
    for item in word:
        length = len(item)
        if length > max_length:
            max_length = length
        return max_length
word= input("Enter a list of words seprated by spaces:")
word=word.split()
result=longestWord(word)
print(f"The length of the longest word is :{result}")

    
