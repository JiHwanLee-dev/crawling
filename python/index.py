from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request



# script파일 안에 chromedriver.exe를 넣어서, driver경로를 제공 할 필요가 없음.

path = '/Users/Administrator/AppData/Local/Programs/Python/Python38-32/Scripts/chromedriver'
driver = webdriver.Chrome()

url = 'https://dtpia.co.kr/Order/Businesscard/Color.aspx'
#url = 'https://dtpia.co.kr/Sub/sub-page-small-quantity.aspx'



driver.get(url)

elem = driver.find_element_by_id('viewOrder')              # 주문내용 
print('elem : '+elem.text)                                           # text를 붙여야 나옴.

elem2 = driver.find_elements_by_class_name('content-title')
# driver.get('http://google.com');
print(elem2)

for value in elem2:
    print('elem2 : '+value.text)


elem3 = driver.find_elements_by_id('total_am_view')
print(elem3[0].text)



#elem4 = driver.find_element_by_class_name('common-detail-text')
#li = driver.find_elements_by_tag_name('span')

#print(li.text)

# css_selector => element에서 오른쪽 마우스 클릭 -> Copy -> Copy selector를 선택하여 CSS Selector 
elem4 = driver.find_elements_by_css_selector('#OrderTabInfo_02 > div > ul > li')
print(elem4)


for value in elem4:
    print('elem4 : '+value.text)



elem44 = driver.find_element_by_css_selector('#pre_img')
img_src = elem44.get_attribute("src")
print('img_src : '+img_src)


# 후가공 메뉴 선택
#elem5 = driver.find_element_by_css_selector('#ProductInfo_yHugagong > div.tap-btn-line > a.btn.btn-3 > div:nth-child(1)')
#elem5.click()


# btn btn-big btn-example -> btn-example
#btn = driver.find_element_by_class_name('active-color active-border')
#btn.click()



# mouseover메뉴가 있을 시 처리 
action = ActionChains(driver)

firstMenu = driver.find_element_by_css_selector('#product-today-view')
action.move_to_element(firstMenu).perform()
secondMenu = driver.find_element_by_css_selector('#gnb-menu-product-today-view > div > div:nth-child(2) > a.menu-cate-title.menu-category-title')
action.move_to_element(secondMenu).perform()

secondMenu.click()


# body > div.page.page-main > div.content-index > div.right-side > div.img-wrapper > div:nth-child(1) > a > img
#body > div.page.page-main > div.content-index > div.right-side > div.img-wrapper > div:nth-child(1)
elem6 = driver.find_element_by_css_selector('body > div.page.page-main > div.content-index > div.right-side > div.img-wrapper')   
img_srcc = elem6.get_attribute("src")

print(elem6.text)
print(img_srcc)

text = elem6.text.split(')')
#body > div.page.page-main > div.content-index > div.right-side > div.img-wrapper

#imgUrl = driver.find_element_by_css_selector('body > div.page.page-main > div.content-index > div.right-side > div.img-wrapper > div:nth-child(1) > a > img')

# /html/body/div[1]/div[2]/div[2]/div[1]/img
#print(text[0])
#num = '1'

print(len(text))

# img라는 폴더안에 해당 이미지를 저장함
#urll = 'https://dtpia.co.kr/imgs/content_image/business-special.jpg'
#urllib.request.urlretrieve(urll, './img/img1.jpg')


img_list = []

# 현재 페이지의 이미지들을 모은 배열을 반복문 돌림
for index,list in enumerate(text):
    num = str(index+1)

    if(num == "15"):
        break
    print(num)
    imgUrl = driver.find_element_by_css_selector('body > div.page.page-main > div.content-index > div.right-side > div.img-wrapper > div:nth-child(' + num + ') > a > img')
    
    # imgUrl = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/img')
    img_src = imgUrl.get_attribute("src")
    print('imgUrl : ' + img_src)
    
    img_list.append(img_src)
    #print(index)
   
    #num = num + 1

print(img_list)


#driver.back()                         # 페이지 뒤로가기 

#print('aa : '+elem6.text)
#elem6.click()
#elem6.click()




#elem7 = driver.find_elements_by_css_selector('body > div.page.page-main > div.content-index > div.right-side > div.img-wrapper')
#print(elem7)
#for value in elem7:
#    print(value.text)



print('hello')

#driver.close()


#OrderTabInfo_02 > div > ul > li > span

