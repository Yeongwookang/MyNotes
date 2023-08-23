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
