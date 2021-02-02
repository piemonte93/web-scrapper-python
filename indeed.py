import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=last&limit={LIMIT}"


def get_last_page():
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


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"] # 해당 태그의 attribute에 접근하는 방법
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {"title": title, "company": company, "location": location, "link": f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed: page {page}")
        result = requests.get(f"{URL}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)

    return jobs