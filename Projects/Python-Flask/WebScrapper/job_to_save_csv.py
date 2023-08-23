from indeed_extractor import extract_indeed_jobs

def job_to_csv(file_name, jobs):
    file = open(f"{file_name}.csv","w", encoding="utf-8 sig")

    file.write("직무, 사명, 위치, 상세, 게시일, 링크 \n")
    for job in jobs:
        file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['description']}, {job['postDate']}, {job['link']}\n")

    file.close()
    print(f"{file_name}.csv 파일이 생성되었습니다.")