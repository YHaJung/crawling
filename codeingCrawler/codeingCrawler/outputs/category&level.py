import csv
import pandas as pd
import re

originSubCategory = []
originCategory = []

lectureName = [] # 강의명 string
price = []  # 가격 int
lectureLink = [] # 강의링크 string
thumbnail = []  # 썸네일 사진링크 string
level = [] # 강의레벨 int(1~5)/정보 없으면 추출/그래도 모르면 6
lecturer = []
siteIdx = [] # 사이트번호 int(기준??)
rating = [] # 평점(나중에 내부 리뷰평점으로 대체) - float1~5
contents = [] # 강의목차 - string
category = []
subCategory = [] # programming language
type =[] # 온라인/오프라인 string on/장소명
language = [] # 언어 한글이면 ko, 영어면 en
totalDuration = []  # 총 강의길이 int 분단위
numOfLectures = [] # 총 강의 개수 int



subCategoryList = {'VR/AR':'가상현실','ajax':'ajax','BlockChain':['블록체인','blockchain'],'GraphQL':'graphql','Kaggle':['캐글','kaggle'],'Reinforcement Learning':['reinforce','강화학습'],'Hadoop':['하둡','hadoop'],'MySQL':'mysql','MongoDB':'mongodb','MariaDB':'mariadb','Php':'php','JPA':'jpa','ios':'ios','JQuery':['jquery','제이쿼리'],
              'Angular':['angular','앵귤러', 'angularjs'],'TypeScript':['타입스크립트','typescript'],'React.js':['리액트','react.js','react'], 'React Native':['리액트네이티브','reactnative'],
               'Html':'html','JavaScript':['자바스크립트','javascript', 'js'],'Scratch':['scratch','스크래치'],'Laravel':['laravel','라라벨'],
               'BootStrap':['부트스트랩','bootstrap'],'Node.js':['노드','node'],'Spring':['스프링','spring'],'Django':['django','장고'],
               'Firebase':['파이어베이스','firebase'],'AWS':['aws','아마존'],'Ruby':['루비','ruby'],'Flask':['flask','플라스크'],'Oracle':['오라클','oracle'],
               'C':'씨언어','C++':'c++','C#':['c#','씨샵'],'Python':['python','파이썬'],'Java':['자바','java'],'Lua':['루아','lua'],'Android':['android','안드로이드'],
               'Swift':['스위프트','swift'],'Flutter':['flutter','플러터'],'Ionic':['아이오닉','ionic'],'Kotlin':['코틀린','kotlin'],'Redux':['redux','리덕스'],
               'TensorFlow':['tensorflow','텐서플로우'],'PyTorch':['파이토치','pytorch'],'Keras':['케라스','keras'],'Pandas':['판다스','pandas'],'Cloud':['클라우드','cloud'],
               'Anaconda':['anaconda','아나콘다'],'Numpy':['넘파이','numpy'],'Azure':'azure','Serverless':['서버리스','serverless'],'Kubernetes':['쿠버네티스','kubernetes'],
               'IoT':'사물인터넷','OpenCV':['오픈씨브이','opencv'],'Unreal Engine':['언리얼','unreal'],'Objective-C':['오브젝티브-c','objective-c'],
               'Unity':['유니티','unity'],'Linux':['리눅스','linux'],'Git':['깃','git'],'OAuth':'oauth','WordPress':['워드프레스','wordpress'],
               'Computer Vision':['컴퓨터비전','computervision'],'Deep Learning':['딥러닝','deeplearning'],'Machine Learning':['머신러닝','machinelearning'],
            'CSS':'css','C':['c','c언어'],'Go':'go ','ROR':' ror','VR/AR':['virtual reality','vr ',' ar '],'IoT':' iot','R':[' r ','r언어']
            }

#subCategoryList2 = {'CSS':'css','JavaScript':' js','C':['c ','c언어'],'Go':'go ','ROR':' ror','VR/AR':['virtual reality','vr ',' ar '],'IoT':' iot','R':[' r ','r언어']}

sub = ['web','app','back-end','fullStack','game','ai','algorithm','network','dataScience','cs']

web =['웹','web','html','css','vue.js','react.js','리액트','react']
app =['app','어플','앱','어플리케이션','모바일','mobile','안드로이드','ios','swift','android','kotlin','flutter','플러터','reactnative','mobile','리액트네이티브']
be = ['laravel','라라벨','ajax','도커','docker','back','server','서버','db','database','데이터베이스','백엔드','sql','aws','php','node','spring','django','노드']
fullStack = ['풀스택','fullstack']
game = ['게임','유니티','unity','game','virtual','vr','가상현실','2d','3d','엔진','unreal','언리얼']
ai = ['DQN','ai ','machinelearning','deeplearning','reinforce','artificial','인공지능','머신러닝','딥러닝','강화학습']
algorithm = ['코딩테스트','알고리즘','algorithm','datastructure','자료구조']
network = ['해킹','hacking','네트워크','보안','암호','5g','security','encypt','악성코드','메타스플로잇','Metasploit']
dataScience = ['hadoop','data','ds','데이터분석','시각화','visualization','pandas','sql','데이터','analytics','분석']
cs = ['수학','확률', '자료구조','알고리즘','운영체제','operatingsystem','computerarchitecture','컴퓨터구조','datastructure','algorithm','softwareengineering','소프트웨어공학','컴퓨터과학','computerscience','statistic']
language2 = ['객체','파이썬','c언어','c++','자바','java','python','자바스크립트','c#','스크래치','scratch','js','기초프로그래밍'] # 가장 마지막에 확인

lv1 = ['begin','기본','기초','basic','기반','start','스타터','처음','초보','입문','초급','first','intro','쉽고','쉬운','쉽게','누구나','이해','일반인','첫','overview', 'easy']
lv3 = ['중급','intermediate','조금 더','활용', 'normal']
lv5 = ['응용','심화','실무','고급','실전','advanced','clone','클론','complex', 'difficult']

with open('KocwCrawlingFile.csv','rt') as f:
    reader = csv.DictReader(f)#확인하기

    for c in reader:
        for k, v in c.items():
            if (k == 'lectureName') : lectureName.append(v)
            elif (k == 'price') : price.append(v)
            elif (k == 'lectureLink') : lectureLink.append(v)
            elif (k == 'thumbnail') : thumbnail.append(v)
            elif (k == 'level') : level.append(v)
            elif (k == 'lecturer') : lecturer.append(v)
            elif (k == 'siteIdx') : siteIdx.append(v)
            elif (k == 'rating') : rating.append(v)
            elif (k == 'contents') : contents.append(v)
            elif (k == 'category') : originCategory.append(v)
            elif (k == 'subCategory') : originSubCategory.append(v)
            elif (k == 'type') : type.append(v)
            elif (k == 'language') : language.append(v)
            elif (k == 'totalDuration') : totalDuration.append(v)
            elif (k == 'numOfLectures') : numOfLectures.append(v)


#띄워쓰기 없애기, keyword를 category에 추가
def check(keyword, list, element, idx):
    for i in list:
        if i in element.lower().replace(" ",""):
            category[idx] = category[idx] + keyword +","
            break

def check2(keyword, list, element, idx):
    status = True
    for elements in sub:
        if elements in category[idx]:
            status = False
            break
    if status is True:
      for i in list:
        if i in element.lower().replace(" ",""):
            category[idx] = category[idx] + keyword +","
            break


count = 0
tmpLecName=""
for e in range(len(lectureName)):
    ''' # 사이트에 따라 tag 혹은 lectureName을 카테고리 분류 위해 사용
    if source[e] == "udacity" or source[e] =="fastcampus" or source[e] =="inflearn":
        tmpLecName = tag[e]
    else:
        tmpLecName = lectureName[e]
    '''
    #tmpLecName = originSubCategory[e]+" "+lectureName[e]
    tmpLecName = lectureName[e] + " " + contents[e]

    category.append("")
    check("web", web, tmpLecName, count)
    check("app", app, tmpLecName, count)
    check("backEnd", be, tmpLecName, count)
    check("fullstack", fullStack, tmpLecName, count)
    check("game", game, tmpLecName, count)
    check("ai", ai, tmpLecName, count)
    check("algorithm", algorithm, tmpLecName, count)
    check("dataScience", dataScience, tmpLecName, count)
    check("network", network, tmpLecName, count)
    check("computerScience", cs, tmpLecName, count)
    check2("language", language2, tmpLecName, count)
    count = count +1
'''
for i in range(len(lectureName)):
    print(lectureName[i]," - ", category[i][:-1])
'''

subIdx=0

for i in range(len(lectureName)):
    subCategory.append("")

tmpSubCategory=""

for k, v in subCategoryList.items():
  for idx in range(len(lectureName)):
    #if originSubCategory[idx].strip() != "":
    #    continue
    ''' # 사이트에 따라 tag 혹은 lectureName을 카테고리 분류 위해 사용
    if source[idx] == "fastcampus" or source[idx] =="udacity" or source[e] =="inflearn":
        tmpSubCategory = tag[idx]
    else:
        tmpSubCategory = lectureName[idx]
    '''

    #tmpSubCategory = re.sub("[:,로/]", " ", originSubCategory[idx]+" "+lectureName[idx])
    tmpSubCategory = re.sub("[:,로/프로그래밍]", " ", lectureName[idx] + " " + contents[idx])
    '''
    if str(type(v)) == "<class 'str'>": # value가 하나
        if v in tmpSubCategory.lower().replace(" ",""):
            subCategory[idx] = subCategory[idx] + k+","
    else:
    '''
    for element in v:
        if element in tmpSubCategory.lower().split():
            subCategory[idx] = subCategory[idx] + k+","
            break
"""
for k, v in subCategoryList2.items():
     for idx in range(len(lectureName)):
          #if originSubCategory[idx].strip() != "":
          #   continue

          ''' # 사이트에 따라 tag 혹은 lectureName을 카테고리 분류 위해 사용
          if source[idx] == "fastcampus" or source[idx] == "udacity" or source[e] =="inflearn":
              tmpSubCategory = tag[idx]
          else:
              tmpSubCategory = lectureName[idx]
          '''
          tmpSubCategory = lectureName[idx]
          '''
          if str(type(v)) == "<class 'str'>":  # value가 하나
              if v in tmpSubCategory.lower():
                  subCategory[idx] = subCategory[idx] + k + ","

          else:
          '''
          for element in v:
              if element in tmpSubCategory.lower().split():
                  subCategory[idx] = subCategory[idx] + k + ","
                  break
"""
for i in range(len(subCategory)):
    if subCategory[i].endswith(','):
       a = subCategory[i][:-1].split(',')
    else:
        a = subCategory[i].split(',')
    new =""
    for element in a:
        if 'React Native' in element:
            a.remove('React.js')
        elif 'Go' in element:
            for k in a:
                if('Django' in k):
                   a.remove('Go')
                   break

    if subCategory[i].count('Java') > 1:
        a.remove('Java')
    for element in a:
        new=new+element+","
    subCategory[i] = new
'''
for i in range(len(originSubCategory)):
    if originSubCategory[i].strip() != "":
        subCategory[i] = originSubCategory[i]
'''
for i in range(len(subCategory)):
    if subCategory[i][:-1].strip() == "":
        subCategory[i] = 'other,'

for i in range(len(category)):
    if category[i][:-1].strip() == "":
        category[i] = 'other,'



#맨 뒤에 콤마 빼기
for i in range(len(subCategory)):
    category[i]=category[i][:-1]
    subCategory[i]=subCategory[i][:-1]

tmpNum = 0

#for element in level:
for element in lectureName:
    tmpValue = 0
    tmpCount = 0

    '''
    if level[tmpNum] != 0 and level[tmpNum].strip() != "":
        tmpNum = tmpNum + 1
        continue
'''
    for i in lv1:
        if i in element.lower():
            tmpValue = tmpValue + 1
            tmpCount = tmpCount + 1
            break
    for i in lv3:
        if i in element.lower():
            tmpValue = tmpValue + 3
            tmpCount = tmpCount + 1
            break
    for i in lv5:
        if i in element.lower():
            tmpValue = tmpValue + 5
            tmpCount = tmpCount + 1
            break
    if(tmpCount!=0):
       level[tmpNum] = float(tmpValue)/tmpCount
    else:
        level[tmpNum] = 0

    tmpNum= tmpNum + 1
'''
print(
    len(lectureName),
    len(price),
    len(lectureLink),
    len(thumbnail),
    len(level),
    len(lecturer),
    len(siteIdx),
    len(rating),
    len(contents),
    len(category),
    len(subCategory),
    len(type),
    len(language),
    len(totalDuration),
    len(numOfLectures)
)
'''
'''
for i in range(len(lectureName)):
    print(lectureName[i], " : ", category[i], " / ", subCategory[i], " / ", level[i])

'''
df1 = pd.DataFrame({
    'lectureName' : lectureName,
    'price':price,
    'lectureLink':lectureLink,
    'thumbnail':thumbnail,
    'level':level,
    'lecturer':lecturer,
    'siteIdx':siteIdx,
    'rating':rating,
    'contents':contents,
    'category':category,
    'subCategory': subCategory,
    'type':type,
    'language' :language,
    'totalDuration' : totalDuration,
    'numOfLectures':numOfLectures,
})

print(df1)

df1.to_csv('KocwCrawlingFile2.csv', encoding='utf-8-sig')





