from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search ():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,"textarea[title = 'Search']").click()
    driver.find_element(By.CSS_SELECTOR, "textarea[title = 'Search']").send_keys("Chatgpt")
    driver.find_element(By.CSS_SELECTOR, "textarea[title = 'Search']").send_keys(Keys.ENTER)

    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID, "search")))

    #find_elements return list of elements
    search_result = driver.find_elements(By.CSS_SELECTOR, "div.g")
    for result in search_result:
        result_text = result.text
        if "ChatGPT" in result_text:
            print("Found 'Chatgpt' in the search result:")

    driver.quit()

