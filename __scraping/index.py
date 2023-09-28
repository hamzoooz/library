# get some quotes from mawdoo3.com
import json
from selenium import webdriver
import webdriver_manager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Create a Firefox WebDriver instance using GeckoDriverManager
driver = webdriver.Firefox( )

# Navigate to the URL
url = "https://mawdoo3.com/%D8%A3%D8%B1%D9%88%D8%B9_%D8%A3%D9%82%D9%88%D8%A7%D9%84_%D8%A7%D9%84%D8%AD%D9%83%D9%85%D8%A7%D8%A1"
driver.get(url)

try:
    # Find the ul element by XPath
    # webdriver_manager driver = new FirFoxDriver();
    # ul_element = driver.find_element(By.xpath('//*[@id="mw-content-text"]/ul[2]' ))
    ul_element =  driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/ul[2]')

    # Get the text content of the ul element
    ul_text = ul_element.text

    # Create a dictionary to store the data
    data = {
        'ul_content': ul_text,
        'url': url
    }

    # Specify the output JSON file path
    output_file_path = 'output.json'

    # Write the data to the JSON file
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to {output_file_path}")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    # Close the WebDriver
    driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By


# def test_eight_components():
#     # driver = webdriver.Chrome()
#     driver = webdriver.Firefox()

#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#     title = driver.title
#     assert title == "Web form"

#     driver.implicitly_wait(0.5)

#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#     text_box.send_keys("Selenium")
#     submit_button.click()

#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"

#     driver.quit()
