import random

def makeEngVoca(vocatxt):
    voca = str(vocatxt)
    vocaTxt = open(voca, 'r')

t = open("voca.txt", 'r')
vocaword = open("vocaword.txt", 'w')
vocamean = open("vocamean.txt", 'w')


wordList = []
meanList = []
for i in range(5):
    (word, space, mean) = t.readline().partition(' ')
    wordList.append(word)
    meanList.append(mean[:-1])

for j in range(len(wordList)):
    vocaword.write(wordList[j] + '\n')
    vocamean.write(wordList[j] + ' ' + meanList[j] + '\n')

print(wordList)
print(meanList)

print(t.readline())
t.close()
vocaword.close()
vocamean.close()