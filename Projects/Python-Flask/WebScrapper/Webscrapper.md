## Selenium을 활용하여 웹스크래퍼 만들기
Selenium 4.11.2 버전을 import 하여 채용사이트인 indeed를 scrapping 해보았다.

#### 개발 환경 세팅

    처음에는 replit으로 개발을 진행했는데, replit은 파이썬 3.10을 사용하고 패키지 설치 및 설정이 힘들어서,
    VSCode로 개발을 진행했다.
    Chrome driver는 매번 맞춰서 파일을 넣기가 어려울것 같아서 크롬을 최신업데이트 하고 
    pypi에 있는 webdriver-manager 모듈을 활용하여 자동 최신화하게 했다.

#### Selenium
    replit으로 할때는 beautifulsoup를 이용해서 하다가 Selenium의 메소드들을 새로 알아야 했다.
    https://www.selenium.dev/documentation/ 공식문서를 참조하면서 해결했다.
<br>
<br>
    
## 결과
Selenium을 활용하여 키워드와 한번에 검색할 양을 정하면 

처음 5개 페이지에 대해 스크랩해서 Excel 파일로 만들어주는 Scrapper를 만들었다.

<details> 
<summary>Scrapper 코드</summary>
    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    def get_page_count(keyword):
        chrome_options = webdriver.ChromeOptions()
    
        # 브라우저 꺼짐 방지 옵션
        chrome_options.add_experimental_option("detach", True)
        service=ChromeService(ChromeDriverManager().install())
    
        # webdriver-manager
        driver = webdriver.Chrome(service=service, options=chrome_options)
        base_url ="https://kr.indeed.com/jobs?q="
        query = f"{keyword}"
        
        driver.get(f"{base_url}{query}")
        
        pagination = driver.find_element(By.XPATH,'//*[@class="jobsearch-LeftPane"]/nav')
        pages = pagination.find_elements(By.TAG_NAME,'div')
        if pages == []:
            driver.quit()
            return 1
        
        count = len(pages)
        if count>=5:
            driver.quit()
            return 5
        else:
            driver.quit()
            return count
    
    def extract_indeed_jobs(keyword, limit=10):
        chrome_options = webdriver.ChromeOptions()
    
        # 브라우저 꺼짐 방지 옵션
        chrome_options.add_experimental_option("detach", True)
        service=ChromeService(ChromeDriverManager().install())
    
        # webdriver-manager
        driver = webdriver.Chrome(service=service, options=chrome_options)
        base_url ="https://kr.indeed.com/jobs"
        pages = get_page_count(keyword)
        results=[]
        
        for page in range(pages):
            request_url= f"{base_url}?q={keyword}&limit={limit}&start={page*limit}"
            driver.get(request_url)
            
            wait = WebDriverWait(driver, 10)
            cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul/li')))
            for card in cards:
                if card.get_attribute('innerText').replace(" ","") != "":
                    jobTitle = card.find_element(By.CLASS_NAME, 'jobTitle')
                    job_data = {
                    'position' : jobTitle.find_element(By.TAG_NAME, 'span').text.replace(","," "),
                    'company': card.find_element(By.CLASS_NAME,'companyName').text.replace(","," "),
                    'location': card.find_element(By.CLASS_NAME,'companyLocation').text.replace(","," "),
                    'description' : card.find_element(By.CLASS_NAME,'job-snippet').text.replace(","," "),
                    'postDate':card.find_element(By.CLASS_NAME,'date').text.replace(","," ").replace("Posted\n",""),
                    'link': card.find_element(By.TAG_NAME,'a').get_attribute('href').replace(","," ")
                    }
                    results.append(job_data)   
        driver.quit()
        return results


</details>
<br>

### 데이터 가공

#### selenium.common.exceptions.NoSuchElementException 

    한번에 검색하는 갯수가 적게 설정하면 문제가 없었지만, 갯수를 늘리니 NoSuchElementException이 나왔습니다.
    처음에는 코드가 잘못된줄 알고 for문에 index도 해본 결과, indeed사이트는 mosaic-afterFifthJobResult 처럼
    5단위로 공백을 보내고 있었다.

#### 해결

    if card.get_attribute('innerText').replace(" ","") != "":
    을 통해 공백을 잘라냈을때 공백이 아니라면이라는 조건을 걸어 해결되었다.

#### ,와 \n이 포함되어 csv파일이 일정한 형태를 가지지 않음
    모든 문자열에 대해 ,를 대체하였는데도 postDate에서 글자 중간에 \n이 있었음
    그 부분도 수정해주니 결과가 나왔다

#### 의문점
    한번에 검색할 양을 늘리면 전체 내용을 긁어오는데 문제는 없지만, 
    pagination은 한번에 5개씩만 보여주기 때문에 전체 내용을 다 긁어오고 싶을 때나
    indeed가 아닌 다른 사이트에서는 검색 쿼리로 limit를 제공하지 않을수도 있는데,
    이를 어떻게 해결해야할지 생각을 해봐야겠다.

<br>

### csv파일로 만들기
csv 파일로 만들어주는 코드이다. 파이썬 기본 라이브러리의 파일 함수를 사용하였다.

utf-8로만 인코딩하면 엑셀등에서 켰을때 글자가 깨져서 utf-8 sig로 인코딩 하였다.

<details> 
<summary>csv파일로 만들기 코드</summary>
 
    from indeed_extractor import extract_indeed_jobs
    
    def job_to_csv(file_name, jobs):
        file = open(f"{file_name}.csv","w", encoding="utf-8 sig")
    
        file.write("직무, 사명, 위치, 상세, 게시일, 링크 \n")
        for job in jobs:
            file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['description']}, {job['postDate']}, {job['link']}\n")
    
        file.close()
        print(f"{file_name}.csv 파일이 생성되었습니다.")
</details>

<br>

### Flask 

keyword와 limit을 쿼리로 하는 페이지를 구현하였다. export 할때 다시 검색하여 하지 않도록 db={} 를 활용하여 임시저장한 뒤
파일로 만들어 다운로드 가능하도록 하였다.
Flask는 부트캠프에서는 간단하게만 해보았는데, 파일처리 등이 스프링보다는 편한 것 같다.

<details> 
<summary>main 코드</summary>
    
    from flask import Flask, render_template, request, redirect, send_file
    from indeed_extractor import extract_indeed_jobs
    from job_to_save_csv import job_to_csv
    
    app = Flask("JobScrapper")
    
    db = {}
    
    @app.route("/")
    def home():
        return render_template("home.html")
    
    @app.route("/search")
    def search():
        keyword = request.args.get("keyword")
        limit = request.args.get("limit")
        
        # 검색어 없으면 홈으로
        if keyword == None or limit == None:    
            return redirect("/")
        
        limit = int(limit)
        file_name = f"{keyword}_{limit}"
        
        if file_name in db:
            jobs = db[file_name]
        
        else: 
            jobs = extract_indeed_jobs(keyword, limit)
            db[file_name] = jobs
        return render_template("search.html", keyword = keyword, limit = limit, jobs = jobs)
    
    @app.route("/export")
    def export():
        keyword = request.args.get("keyword")
        limit = request.args.get("limit")
        limit = int(limit)
        
        file_name = f"{keyword}_{limit}"
        
        if keyword == None or file_name not in db:    
            return redirect("/")
        
        else:
            job_to_csv(file_name, db[file_name])
            return send_file(f"{file_name}.csv", as_attachment=True)
    
    app.run("localhost")
</details>
