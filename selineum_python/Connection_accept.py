import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



# linkedin Network_Accepting #    

# step 0 : you need chrome for this. Also install modules :
# pip install selenium && pip install webdriver_manager && pip install tinydb

# 

driver = webdriver.Chrome(ChromeDriverManager().install())
# ************open Linkedin*****************
driver.get("https://www.linkedin.com/login")

# *****find and set  the username $ password elements 
driver.find_element_by_id("username").send_keys("isha19@navgurukul.org")
driver.find_element_by_id("password").send_keys("ishabharti")
# ***********get the submit buttonn and click on it***************
driver.find_element_by_css_selector(".btn__primary--large").click()
# ***********btn__primary--large e took from signupp css inspect **********
# *************open Invitation Page*******************
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
# *******Get all the available Invtation Accept Bottom***********************
acceptButtons=[]    

while len(acceptButtons)==0:
        acceptButtons=driver.find_elements_by_xpath("//button[@class='invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
# Accept connections by clicking the buttons
for button in acceptButtons:            
        button.click()
        sleep(2)


























































































































































