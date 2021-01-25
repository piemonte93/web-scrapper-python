import requests
from bs4 import BeautifulSoup ## BeautifulSoup: 데이터를 추출하는 라이브러리

## requests Obj 안의 get()메소드 이
indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=last&limit=50")

## soup = BeautifulSoup(html_doc, 'html.parser') 형태로 사용
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

## indeed_soup에서 모은 html정보에서 div 태그에 클래스가 pagination인 요소를 리스트로 반환
pagination = indeed_soup.find("div", {"class":"pagination"})

## pagination에서 a 태그인 요소를 리스트로 반환
pages = pagination.find_all('a')
spans = [] ## span을 저장할 리스트

## pages의 값을 추출 및 확인하면서 span 태그인 것을 찾아서 spans 리스트에 추가
for page in pages:
    spans.append(page.find("span"))

## spans의 값을 마지막 요소를 제외하고 전부 spans로 저장
spans = spans[:-1]