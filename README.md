# chrawling - 2021.01.06
##framework : 스크래피
참고 : https://livedata.tistory.com/26

# 사이트 리스트
egghead, 칸 아카데미, 구름에듀, k-mooc, KOCW

# 대상
lectureName # 강의명 string 
price # 가격 int  
lectureLink # 강의링크 string  
thumbnail # 썸네일 사진링크 string  
level # 강의레벨 int(1~5)/정보 없으면 추출/그래도 모르면 6  
lecturer  
siteIdx # 사이트번호 int
rating # 평점(나중에 내부 리뷰평점으로 대체) - float1~5  
contents # 강의목차 - string  
category  
subCategory # programming language  
type # 온라인/오프라인 string on/장소명  
language  # 언어 한글이면 ko, 영어면 en  
totalDuration  # 총 강의길이 int 분단위  
numOfLectures  # 총 강의 개수 int  
