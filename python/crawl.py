from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import requests
import pymysql.cursors

# 데이터베이스 연결정보
conn = pymysql.connect(
    host = '13.209.70.57',
    user = 'root',
    password = 'Zocm6GlxWQPS',
    db = 'movie_work',
    charset = 'utf8'
)   

cursor = conn.cursor()

# script파일 안에 chromedriver.exe를 넣어서, driver경로를 제공 할 필요가 없음.

path = '/Users/Administrator/AppData/Local/Programs/Python/Python38-32/Scripts/chromedriver'
driver = webdriver.Chrome()


# url = 'https://www.megabox.co.kr/theater/list'
url = 'https://www.megabox.co.kr/movie'
# url = 'https://www.naver.com'
# url = 'https://www.megabox.co.kr'
# url = 'https://www.megabox.co.kr/booking'
# url = 'https://movie.yes24.com/Movie/Ticket'

driver.get(url)



#      네이버 검색창 클릭 
# elem1 = driver.find_elements_by_css_selector('#query')
# elem1[0].send_keys("aaa")

# searchBtn = driver.find_element_by_css_selector('#search_btn > span.ico_search_submit')
# searchBtn.click()

city = driver.find_elements_by_css_selector('#contents > div > div.theater-box > div.theater-place > ul > li > button')
theater = driver.find_elements_by_css_selector('#contents > div > div.theater-box > div.theater-place > ul > li > div > ul')

test = driver.find_elements_by_css_selector('#contents > div > div.theater-box > div.theater-place > ul > li')
# theater_2 = driver.find_elements_by_css_selector('#contents > div > div.theater-box > div.theater-place > ul > li.on > div > ul > li > a')


# TEST함수
def testDB():
    try:
        # sql = "select * from user where id = 'aa'"
        # cursor.execute(sql)
        # result = cursor.fetchall()
        # print('result : ' + str(result))

        sql = "insert into test_table(sno, name, addr) values(%s, %s, %s)"
        cursor.execute(sql, (2, 'name2', 'addr2'))
        conn.commit()                                     # commit을 해줘야 insert가 실행됨.
        print('??')
    except Exception as e:
        print('err : ' + e)
    finally:
        conn.close()

# testDB()

# 데이터베이스에 극장정보를 넣는 함수
def insertDB(nmt_cd, city, theater):
    try:
        sql = "insert into nationwide_movie_theater(nmt_cd, city, theater) values(%s, %s, %s)"
        cursor.execute(sql, (nmt_cd, city, theater))
        conn.commit()                                     # commit을 해줘야 insert가 실행됨.
    
    except Exception as e:
        print('err : ' + e)


# 전국 지역의 극장 크롤링 함수
def movie_theater():
    # url = 'https://www.megabox.co.kr/theater/list'
    btn = driver.find_elements_by_css_selector('#contents > div > div.theater-box > div.theater-place > ul > li > button')
    
    mCity = ''

    # 전국에 있는 각 극장의 코드값
    nmt_cd = 900

    # 전국 도시에 있는 메가박스 영화관 크롤링 코드 
    for values in btn:
        nmt_cd = nmt_cd + 100
        #print('theater : '+ values.text)
        print('city : '+ "<" + values.text + ">")
        values.click()
        theaters = driver.find_elements_by_css_selector('#contents > div > div.theater-box > div.theater-place > ul > li.on > div > ul > li > a')
        
        for valuess in theaters:
            nmt_cd = nmt_cd + 1
            print('theater : ' +  ',' + valuess.text + 'nmt_cd : ' + str(nmt_cd))
            # print('city : '+ "<" + values.text + ">")
            # insertDB(nmt_cd, values.text, valuess.text)
            

        
        #print('theater : '+ "[" + theaters[0].text + ","+ "]")

        time.sleep(2)

# movie_theater()
# movieList > li:nth-child(2) > div.movie-list-info > img
#movieList > li:nth-child(3) > div.movie-list-info > div.movie-score > a > div.summary

def movie_info():
    #movieList
    # thumbnail = driver.find_elements_by_css_selector('#movieList > li > div.movie-list-info > img')
    summary = driver.find_elements_by_css_selector('#movieList > li > div.movie-list-info > div.movie-score > a ')
    more = driver.find_elements_by_css_selector('#btnAddMovie')
    # print('list11 : ' + str(thumbnail))
    print('list11 : ' + str(summary))

    # for lists in thumbnail:
        # print()
        # print('img_src : ' + lists.get_attribute('src'))
    print('length : ', len(summary))
    for lists in summary:
        # print()
        print('summary : ' + lists.text)

    print('more : ' + str(more))

    img_list = []

    while True:

        try:
            print('str(more) : ' + str(more[0]))
            if more[0]:
                print('참')
                img_list.append(more[0].text)
                more[0].click()
                time.sleep(0.5)

        except Exception as e:
            print(e)
            print('영화 페이지가 더이상 없음.')

         

            break


    print('뚜루')
    print('list : ' + str(img_list))

    for lists in img_list:
            print('lists : ' + lists.text) 
    
    # thumbnail = driver.find_elements_by_css_selector('#movieList > li > div.movie-list-info > img')
    # thumbnail_src = thumbnail.get_attribute('src')
    # print('thumbnail : ' + thumbnail_src)

    # for lists in thumbnail_src:
    #         print('lists : ' + lists.text)
       

    
    

    

movie_info()



