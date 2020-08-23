from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException 
import regex as re
import time

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

#to prevent chrome from showing that it is being controlled by an automated software/script
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)  

driver = webdriver.Chrome()  
driver.get("https://www.youtube.com/playlist?list=PL_whQ8VqOnGhRCi0QtSnhWpvJbUMOc2gG")
wait = WebDriverWait(driver, 10)
wait.until(page_is_loaded)

'''amv_titles = []
x_arg = "//span[contains(@id,'video-title')]"
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
print(group_title.text)
#amv_titles.append(group_title.text)'''


SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
'''
while True:


    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

'''
for i in range(2):
	html = driver.find_element_by_tag_name('html')
	html.send_keys(Keys.END)
	time.sleep(5)


x_arg = "//span[contains(@id,'video-title')]"
#video_title = driver.find_elements_by_xpath("x_arg")
video_title = driver.find_elements_by_id("video-title")
print(type(video_title))

amv_titles = []
text_file = open("AMV_titles.txt", "w", encoding='utf-8')
for title in video_title:
	try:
		text_file.write(title.text +"\n")
	except UnicodeEncodeError:
		continue
text_file.close()


