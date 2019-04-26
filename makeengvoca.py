import random

def makeEngVoca(vocafile, quesNum, vocaword, vocamean): # 인자로 단어파일(str), 문항수(int), 만들어질 단어장파일이름(str), 단어정답파일이름(str)을 받음

    try:
        if vocaword == '':
            vocaword = 'vocaword'

        if vocamean == '':
            vocamean = 'vocamean'

        vocaTxt = open(vocafile + 'txt', 'r')
        vocaWord = open(vocaword + 'txt', 'w')
        vocaMean = open(vocamean + 'txt', 'w')
        wordList = []
        meanList = []

        for i in range(10):
            (word, space, mean) = vocaTxt.readline().partition(' ')
            wordList.append(word)
            meanList.append(mean[:-1])

        if quesNum > len(wordList):
            return "만들려는 문항수가 단어 수보다 많습니다!"

        randomQuesNumber = random.sample(range(0,len(wordList)), quesNum)

        for j in randomQuesNumber:
            vocaWord.write(wordList[j] + '\n')
            vocamean.write(wordList[j] + ' ' + meanList[j] + '\n')

        vocaTxt.close()
        vocaWord.close()
        vocaMean.close()
        return "제작 완료"
    except FileNotFoundError:
        return vocafile + "이름을 가진 단어 파일이 없습니다!"
