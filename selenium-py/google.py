from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

# 크롬 웹 드라이버를 연다.
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=en&ogbl")
# 구글 검색창 찾기
elem = driver.find_element(By.NAME, "q")
# 구글 검색어
elem.send_keys("풍선")
# 엔터키 입력
elem.send_keys(Keys.RETURN)

#스크롤 시간 설정
SCROLL_PAUSE_TIME = 2

# Get scroll height
# execute_script : javascript 를 실행하는 코드 
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    # 브라우저 끝까지 스크롤 내린다.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    # 0.5초 동안 기다림
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    #이전과 내린 스크롤의 높이가 같다면
    if new_height == last_height:
        try:
            #결과 더보기 버튼이 있으면 클릭
            driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
        except:
            break
    last_height = new_height

#이미지 엘리먼트 선택 및 클릭
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
#이미지 반복문
for image in images:
    try : 
        image.click()
        #3초지연
        time.sleep(2)
        #선택한 큰 이미지 선택후 src 주소 선택
        imgUrl = driver.find_element(By.CSS_SELECTOR, "#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id.b0vFpe > div > a > img").get_attribute("src")
        #이미지 다운로드
        urllib.request.urlretrieve(imgUrl, str(count) + '.jpg')
        count = count + 1
    except :
        pass

driver.close()