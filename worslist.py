s=input(" enter a sentence:");
print(s)
wordsList =s.split()
print ( wordsList)
for i in wordsList:
    print (f"{i} occures {wordsList.count(i)}times")
