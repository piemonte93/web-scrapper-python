import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=last&limit={LIMIT}"


def extract_indeed_pages():
    # requests Obj 안의 get()메소드 이용
    result = requests.get(URL)

    # soup = BeautifulSoup(html_doc, 'html.parser') 형태로 사용
    soup = BeautifulSoup(result.text, 'html.parser')

    # indeed_soup에서 모은 html정보에서 div 태그에 클래스가 pagination인 요소를 리스트로 반환
    pagination = soup.find("div", {"class": "pagination"})

    # pagination에서 a 태그인 요소를 리스트로 반환
    links = pagination.find_all('a')
    pages = []  # span을 저장할 리스트

    # pages의 값을 추출 및 확인하면서 span 태그인 것을 찾아서 spans 리스트에 추가
    # 마지막 요소는 제외 (다음 페이지로 넘기는 <a>라서 제외, 숫자가 아)
    for link in links[:-1]:
        pages.append(int(link.string))
    # 마지막 페이지를 저장
    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page * LIMIT}")
        print(result.status_code)