import random

def makeEngVoca():
    vocaTxt = open("voca.txt", 'r')
    vocaword = open("vocaword.txt", 'w')
    vocamean = open("vocamean.txt", 'w')


    wordList = []
    meanList = []
    for i in range(10):
        (word, space, mean) = vocaTxt.readline().partition(' ')
        wordList.append(word)
        meanList.append(mean[:-1])

    for j in range(len(wordList)):
        vocaword.write(wordList[j] + '\n')
        vocamean.write(wordList[j] + ' ' + meanList[j] + '\n')

    vocaTxt.close()
    return wordList, meanList

wordList, meanList = makeEngVoca()
print(wordList)
print(meanList)