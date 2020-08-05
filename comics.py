from selenium import webdriver
from PIL import Image
import os
from bs4 import BeautifulSoup
import requests
import time

driver = webdriver.Chrome('./chromedriver')


def episode(start, end):
    for x in range(start, end+1):
        if not os.path.exists(f'./{x}'):
            os.mkdir(f'./{x}')
        # Change the url below according to your favourite comics!
        comics_url = 'https://i.mangabus.xyz/comic/comic-653.html?ch={episode}-{page}'
        driver.get(f'https://i.mangabus.xyz/comic/comic-653.html?ch={x}-')
        soup = BeautifulSoup(driver.page_source, 'lxml')
        page_num = int(soup.find(id='pagenum').text.split('/')[1].strip('頁'))

        for i in range(page_num):
            driver.get(comics_url.format(episode=x, page=i+1))
            image = driver.find_element_by_id('TheImg').get_attribute('src')
            res = requests.get(image)
            with open(f'./{x}/{i}.jpg', 'wb') as param:
                param.write(res.content)
            time.sleep(0.5)


start = int(input('which episode to start from?'))
end = int(input('which episode to end at?'))
episode(start, end)
driver.quit()
print('Done! Enjoy your comics!')
