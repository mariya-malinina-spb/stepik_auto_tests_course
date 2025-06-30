from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def sum(x,y):
  return str(x+y)
  
  
try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x1 = x1_element.text
    x2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    x2 = x2_element.text
    y = int(x1)+int(x2)  
    text=str(y)  
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.click()
    browser.find_element(By.TAG_NAME, "select").click()
    select.select_by_visible_text(text)
    #text=[value=\"sum(x1,x2)\"]
    #browser.find_element(By.CSS_SELECTOR, text).click()    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
