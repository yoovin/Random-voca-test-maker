랜덤 단어시험 제작 프로그램
=========================

* ## 사용시 유의사항
  * Python 3.6으로 제작되었습니다.
  * 단어장 파일은 실행파일과 같은 폴더안에 있어야합니다.
  * 단어장 파일의 Voca와 Mean은 공백(' ')으로 구분합니다.
  * 단어장 파일에는 빈 줄이 있으면 안됩니다. (빈 줄이 있으면 끊겨요)
  * 단어시험지에는 총 단어갯수중 입력값갯수만큼 랜덤으로 선택됩니다.
  * 원본 단어장의 수보다 항목이 많은 단어시험장은 만들 수 없습니다.
  * 단어장의 파일 이름은 무조건 적어야합니다.
  * 문항수는 적어도 1개이상 입력해야합니다.
  * 단어장의 유니코드는 UTF-8을 권장합니다.

* ### 지원언어
  * 한국어 (Korean)
  * 영어 (English)
  * 일본어 (Japanese)
  
## 사용예시
![00](https://user-images.githubusercontent.com/35561369/56840283-a6ec6d80-68c1-11e9-9f6f-77884cf0dda9.PNG)
#### 저장소의 Randomvocatest.exe파일을 받아주세요

![01](https://user-images.githubusercontent.com/35561369/56840284-a7850400-68c1-11e9-8ac0-c33fcf4afa63.PNG)

#### 단어가 쓰여져있는 txt파일을 준비합니다.
#### 단어장 txt파일은 exe파일과 같은 폴더 안에 있어야합니다.
#### 단어장의 텍스트는 index를 매기지 마세요.

![02](https://user-images.githubusercontent.com/35561369/56840285-a7850400-68c1-11e9-8ee9-3eca3432a40d.PNG)

#### 단어장 파일이름, 단어시험지 파일이름, 단어정답지 파일이름, 만들어질 문항 수를 각각 입력해줍니다.
#### 단어시험지와 정답지의 이름을 입력하지않고 넘어갈 시 파일 이름은 Default값으로 정해집니다.
#### 각 항목은 엔터로 넘어가 줍니다.

![03](https://user-images.githubusercontent.com/35561369/56840286-a7850400-68c1-11e9-88db-0dcdc991317e.PNG)

#### 제작이 완료되면 제작 완료라 뜨고, 엔터키를 누르면 프로그램창이 닫힙니다.

![04](https://user-images.githubusercontent.com/35561369/56840287-a7850400-68c1-11e9-9d41-dd6ea580f4a8.PNG)

#### 프로그램이 들어있는 폴더를 확인하면 만들어진 단어장과 정답이 있습니다.

![05](https://user-images.githubusercontent.com/35561369/56840288-a81d9a80-68c1-11e9-815b-787ebde024d4.PNG)

#### 단어장에는 영어단어(원본 단어장의 공백앞에 있는 단어)만 입력되었고 정답지에는 단어와 뜻이 함께 입력됩니다.

![일본어 지원](https://user-images.githubusercontent.com/35561369/56838705-faf35400-68b9-11e9-86fe-db8b9baa0835.PNG)

#### 일본어 단어 또한 사용 가능 합니다.

## 기능추가
![인덱스추가](https://user-images.githubusercontent.com/35561369/56837146-54588480-68b4-11e9-9548-039707d70087.PNG)

### 단어장의 단어들에 자동으로 index를 매기게 기능을 추가했습니다. (19/04/27)
