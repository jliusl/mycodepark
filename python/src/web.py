from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from contextlib import contextmanager

@contextmanager
def browser_session():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    try:
        browser.set_window_size(1200, 800)
        yield browser
    finally:
        browser.quit()

with browser_session() as browser:
    browser.get("https://www.baidu.com")
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, "//*[@id='chat-textarea']").send_keys("中科曙光")
    browser.find_element(By.XPATH, "//*[@id='chat-submit-button']").click()
    wait_obj = WebDriverWait(browser, 10, 1)
    wait_obj.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content_left"))
    )
    browser.get_screenshot_as_file("baidu_headless.png")

