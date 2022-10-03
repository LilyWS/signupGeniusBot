from operator import sub
from time import sleep
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#python main.py https://www.signupgenius.com/go/8050848afa62ba1fb6-wohho "12:00pm - 2:00pm"

driver = webdriver.Firefox()
driver.get(sys.argv[1])

specifiedRow = driver.find_element(By.XPATH, f'//*[contains (text (),"{sys.argv[2]}")]/ancestor::tr[1]')
signupCheckBox = specifiedRow.find_element(By.NAME, "siid")
driver.execute_script("arguments[0].scrollIntoView();", signupCheckBox)
signupCheckBox.click()
submitButton = driver.find_element(By.CLASS_NAME, 'giantsubmitbutton')
print(specifiedRow.text)
print(submitButton.text)
submitButton.click()

timeout = 30

try:
    element_present = EC.presence_of_element_located((By.NAME, 'btnSignUp'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out :(")

sleep(1)

firstNameInput = driver.find_element(By.ID, 'firstname')
lastNameInput = driver.find_element(By.ID, 'lastname')
emailInput = driver.find_element(By.ID, 'email')
signUpBtn = driver.find_element(By.NAME, 'btnSignUp')
print(firstNameInput)
firstNameInput.send_keys(sys.argv[3])
lastNameInput.send_keys(sys.argv[4])
emailInput.send_keys(sys.argv[5])
signUpBtn.click()
sleep(5)
driver.close()