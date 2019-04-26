import makeengvoca

fileName = input("단어장의 파일 이름을 입력해주세요 .txt 불필요 : ")
wordFileName = input("단어 시험이 만들어질 파일의 이름을 입력해주세요 .txt 불필요 (Default file name : vocaword) : ")
meanFileName = input("단어 정답이 만들어질 파일의 이름을 입력해주세요 .txt 불필요 (Default file name : vocamean) : ")
questionNumber = int(input("만들어질 문항 수를 입력해주세요 (단어장의 문항 수 보다 적은 수 여야함) : "))


if wordFileName == '':
    wordFileName = 'vocaword'

if meanFileName == '':
    meanFileName = 'vocamean'

fileName = fileName + '.txt'
wordFileName = wordFileName + '.txt'
meanFileName = meanFileName + '.txt'

print(makeengvoca.makeEngVoca(fileName, questionNumber, wordFileName, meanFileName))