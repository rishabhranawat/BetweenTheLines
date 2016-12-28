from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")

email = driver.find_element_by_id("email")
email.send_keys("rishabhranawat@yahoo.com")

password = driver.find_element_by_id("pass")
password.send_keys("zinnialondon!!")

button = driver.find_element_by_id("loginbutton")
button.click()

url = "https://www.facebook.com/AllTrapNation/videos/1174676259234742"
driver.get(url)

views = driver.find_element_by_class_name("_1t6k")
print(views.text)

driver.close()