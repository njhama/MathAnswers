from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the Quizlet login page
driver.get('https://google.com')

# The target URL you are waiting for
target_url = 'https://quizlet.com/explanations/textbook-solutions/a-first-course-in-probability-8th-edition-9780136033134/chapter-1-problems-2-87d63a01-8f85-4854-af57-0fb9515e851a'

# Loop to keep checking the current URL
while True:
    current_url = driver.current_url
    if current_url == target_url:
        print('Done')
        break
    else:
        time.sleep(1)  # Sleep for a short time before checking the URL again

# Rest of your code
# Keep the browser open for an extended period (or remove this if not needed)
time.sleep(1000)
# Close the browser when you're done
# driver.quit()
