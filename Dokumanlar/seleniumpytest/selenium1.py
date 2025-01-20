from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def setup_driver():
    servcie = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servcie)
    return driver

driver = setup_driver()
wait = WebDriverWait(driver, 10) # Explicit wait

# driver = webdriver.Chrome()

def action_chain_example():
    driver = setup_driver()
    actions = ActionChains(driver)

    try:
        def hover_element(element):
            actions.move_to_element(element).perform()

        def drag_and_drop(source, target):
            actions.drag_and_drop(source, target).perform()
        
        def comlex_action(element):
            actions.move_to_element(element)\
                .click_and_hold().move_by_offset(100, 100).release().perform()

    finally:
        driver.quit()

try:
    driver.get("https://www.google.com")
    # driver.implicitly_wait(10)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q"), timeout=10))
    search_box.send_keys("Selenium")
    button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
    # driver.execute_script("arguments[0].click();", button)
    button.click()
    

    #######################################################
    time.sleep(3)

    # search_box = driver.find_element(By.NAME, "q")
    # search_box.send_keys("Selenium")
    # search_box.submit()
    # time.sleep(3)
    print(driver.get_screenshot_as_png())
except:
    pass
finally:
    driver.quit()