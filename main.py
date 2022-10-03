from operator import sub
from time import sleep
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.signupgenius.com/go/8050848afa62ba1fb6-wohho")

specifiedRow = driver.find_element(By.XPATH, '//*[contains (text (),"12:00pm - 2:00pm")]/ancestor::tr[1]')
signupCheckBox = specifiedRow.find_element(By.NAME, "siid")
driver.execute_script("arguments[0].scrollIntoView();", signupCheckBox)
signupCheckBox.click()
submitButton = driver.find_element(By.CLASS_NAME, 'giantsubmitbutton')
print(specifiedRow.text)
print(submitButton.text)
submitButton.click()

sleep(5) #wait for page load, will use selenium wait function later

firstNameInput = driver.find_element(By.ID, 'firstname')
lastNameInput = driver.find_element(By.ID, 'lastname')
emailInput = driver.find_element(By.ID, 'email')
signUpBtn = driver.find_element(By.NAME, 'btnSignUp')
print(firstNameInput)
firstNameInput.send_keys('Lily')
lastNameInput.send_keys('Sperber')
emailInput.send_keys('stranger1212ss23@gmail.com')
signUpBtn.click()
sleep(5)
driver.close()