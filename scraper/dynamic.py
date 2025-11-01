from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def fetch_dynamic_chapters(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # Example: scrape chapter list
    chapters = [a.get_attribute('href') for a in driver.find_elements('css selector', 'a.chapter')]
    driver.quit()
    return chapters
  
