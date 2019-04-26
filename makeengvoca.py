import random

def makeEngVoca(vocafile, quesNum): # 인자로 단어파일(str)과 문항수(int)를 받음
    vocaTxt = open(vocafile, 'r')
    vocaword = open("vocaword.txt", 'w')
    vocamean = open("vocamean.txt", 'w')
    wordList = []
    meanList = []

    for i in range(10):
        (word, space, mean) = vocaTxt.readline().partition(' ')
        wordList.append(word)
        meanList.append(mean[:-1])


    randomQuesNumber = random.sample(range(0,len(wordList)), quesNum)

    for j in randomQuesNumber:
        vocaword.write(wordList[j] + '\n')
        vocamean.write(wordList[j] + ' ' + meanList[j] + '\n')

    vocaTxt.close()
    vocaword.close()
    vocamean.close()
    return wordList, meanList

wordList, meanList = makeEngVoca('voca.txt', 5)
print(wordList)
print(meanList)