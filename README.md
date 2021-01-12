# chrawling - 2021.01.06~
##framework : 스크래피
참고 : https://livedata.tistory.com/26

# 사이트 리스트
egghead, 칸 아카데미(제외가 나을 듯. 형식 너무 안맞음), 구름에듀, k-mooc, KOCW

# 대상
주제(카테고리), 서브 카테고리, 강사, 수업 횟수(강의개수), 총 강의시간, 수강가능기간, 교육과정(목차), 제목, 사이트, 언어(한글,영어 등), 자막(유무,언어), 가격, 평점(나중에 내부 리뷰평점으로 대체), 난이도, 종류(인강), 썸네일, 링크, 코스 유무

item['main_category']//주제(카테고리)
item['sub_category']//서브 카테고리
item['lecturer']//강사
item['num']//수업 횟수(강의개수)
item['time']//총 강의시간(분)
item['period']//수강가능기간
item['content']//교육과정(목차)
item['title']  //제목
item['site']//사이트
item['language']// 언어(한글,영어 등)
item['subtitle']//자막(유무,언어)
item['price']//가격
item['rate']//평점(나중에 내부 리뷰평점으로 대체)
item['level']// 난이도
item['kind'] = "온라인 강의"//종류(인강)
item['thumbnail']//썸네일
item['url'] //링크
item['course']//코스 유무
