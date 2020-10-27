from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from selenium import webdriver
verb = "ser"
# def get_url(verb = ""):
url = "https://www.spanishdict.com/conjugate/" + verb
# page = urlopen(url)
# html = page.read().decode("utf-8")

#   # return url

# # url = get_url(verb)
# soup = BeautifulSoup(html, "html.parser")
# # info = soup.find("div._3AKO-pN7")
# # info2 = soup.find("div", id="conjugation-content-wrapper")
# # # print(info2.prettify())

# # div._3AKO-pN7
# div._3AKO-pN7
# class="_1btShz4h _3HlR1KX5 P-yt87tk _1b8PdQhU" - unique class for the gerund of verb
# driver = webdriver.Firefox(executable_path=r'C:\Users\ghisl\AppData\Local\Programs\Python\Python39\geckodriver.exe')

driver = webdriver.Firefox()
driver.get(url)
html = driver.page_source
sel_soup = BeautifulSoup(html, "html.parser")
# info = sel_soup.find("div", class_="_2xfncFkp")
def get_gerund(soup=sel_soup):
  info = sel_soup.find("div", class_="_2xfncFkp")
  gerund = info.get_text()
  return gerund

print(get_gerund(sel_soup))

"""
There is the translation of infinitive as header, which is nice
"""
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import re
# from selenium import webdriver
# verb = "ser"

# url = "https://www.spanishdict.com/conjugate/" + verb

# driver = webdriver.Firefox()
# driver.get(url)
# html = driver.page_source
# sel_soup = BeautifulSoup(html, "html.parser")
# def get_gerund(soup=sel_soup):
#   info = sel_soup.find("div", class_="_2xfncFkp")
#   gerund = info.get_text()
#   return gerund
def highlight(element):
    """Highlights a Selenium webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, s)
    orignal_style = element.get_attribute('style')
    apply_style("border: 4px solid red")
    if (element.get_attribute("style")!=None):
        time.sleep(5)
    apply_style(orignal_style)
# print(get_gerund(sel_soup))
# info = driver.find_element_by_class_name("_2xfncFkp")
# print(type(info))
# webdriver.ActionChains(driver).move_to_element(info).perform()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Navigate to url
driver.get("https://www.spanishdict.com/conjugate/ser")
# Store 'google search' button web element
Information = driver.find_element(By.ID,"conjugation-content-wrapper")
specific = Information.find_elements_by_class_name("_2xfncFkp")
print(specific[0].text, specific[1]. text)
result = []
for i in specific:
  print(i.text)
  result.append(i.text)
print(result)
# highlight(searchBtn)
# print(searchBtn)
# Perform double-click action on the element
# webdriver.ActionChains(driver).move_to_element(Information).perform()
# _1btShz4h _3HlR1KX5 P-yt87tk _1b8PdQhU
print(driver.current_url, driver.title)

driver.quit()
