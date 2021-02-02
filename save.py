import csv


def save_to_file(jobs):
    file = open("jobs.csv", mode="w")  # 쓰기 전용 jobs.csv 파일 생성
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))  # key값 제외하고 value값만 가져오기
        # list()를 이용하여 리스트로 저장. list 사용하지 않으면 dict_value()로 반환