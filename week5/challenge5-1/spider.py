import json
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

results = []

def parse(response):
    for comment in response.css('div.comment-list-item'):
        result = {}
        result['name'] = comment.xpath('.//a[@class="username"]/text()').extract_first().strip()
        result['content'] = comment.xpath('.//p/text()').extract_first()
        results.append(result)
    print(results)

def has_next(response):
    next = response.xpath('//li[@class="next-page"]')
    return next


def goto_next(driver):
    next = driver.find_element_by_xpath('//li[@class="next-page"]/a')
    next.click()


def wait(driver,page):
    WebDriverWait(driver,10).until(
        EC.text_to_be_present_in_element(
            (By.XPATH,'//ul[@class="pagination"]/li[@class="active"]'),
            str(page)
            )
        )


def spider():
    driver = webdriver.Chrome()
    url = 'http://www.shiyanlou.com/courses/427'
    driver.get(url)
    page = 1
    while True:
        wait(driver,page)

        html = driver.page_source

        response = HtmlResponse(url=url,body=html.encode('utf8'))

        parse(response)

        if not has_next(response):
            break
        page += 1
        goto_next(driver)

    with open('comments.json','w') as f:
        f.write(json.dumps(results))

if __name__ == '__main__':
    spider()
