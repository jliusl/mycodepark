from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
browser.set_window_size(1200, 800)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get("https://www.baidu.com")
browser.implicitly_wait(5)
browser.find_element(By.ID, "kw").send_keys("selenium")
browser.find_element(By.CSS_SELECTOR, "#su").click()
wait_obj = WebDriverWait(browser, 10)
wait_obj.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#content_left"))
)
browser.get_screenshot_as_file("baidu_headless.png")