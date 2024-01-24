from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')

wait = WebDriverWait(driver, 120)

# Waiting for the Google Search button to be clickable as a placeholder for user interaction.
wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))

# Collect all div elements.
div_elements = driver.find_elements(By.TAG_NAME, 'div')

for div in div_elements:
    # Setting up an action chain to hover over and click the element.
    actions = ActionChains(driver)
    actions.move_to_element(div).click().perform()

    # Retrieving the id and class of the div.
    div_id = div.get_attribute('id')
    div_class = div.get_attribute('class')

    # Printing the id and class if they exist.
    if div_id:
        print(f"Div with id: {div_id} clicked.")
    elif div_class:
        print(f"Div with class: {div_class} clicked.")
    else:
        print("Div with no id or class clicked.")

# Taking a screenshot.
driver.save_screenshot('screenshot.png')
driver.quit()
