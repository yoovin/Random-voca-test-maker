import makeengvoca

while True:
    fileName = input("단어장의 파일 이름을 입력해주세요 .txt 불필요 : ")
    if fileName != '':
        break
    else:
        print("단어장의 파일 이름은 무조건 입력해주세요!")

wordFileName = input("단어 시험이 만들어질 파일의 이름을 입력해주세요 .txt 불필요 (Default file name : vocaword) : ")
meanFileName = input("단어 정답이 만들어질 파일의 이름을 입력해주세요 .txt 불필요 (Default file name : vocamean) : ")

while True:
    questionNumber = input("만들어질 문항 수를 입력해주세요 (단어장의 문항 수 보다 적은 수 여야함) : ")
    if questionNumber == '':
        print("문항 수는 무조건 입력해야합니다.")
    elif int(questionNumber) <= 0:
        print("문항 수는 1이상이어야 합니다.")
    else:
        questionNumber = int(questionNumber)
        break


if wordFileName == '':
    wordFileName = 'vocaword'

if meanFileName == '':
    meanFileName = 'vocamean'

fileName = fileName + '.txt'
wordFileName = wordFileName + '.txt'
meanFileName = meanFileName + '.txt'

print("")
print(makeengvoca.makeEngVoca(fileName, questionNumber, wordFileName, meanFileName))
print("")
input("엔터키를 누르면 종료됩니다.")
