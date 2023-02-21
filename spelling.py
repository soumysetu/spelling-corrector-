from textblob import TextBlob
words = input("Enter the string : ")
word = [words]


corrected_words = []
for i in word:
    corrected_words.append(TextBlob(i))
    
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")
