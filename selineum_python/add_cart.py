import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




# Add to cart in Flipkart   

# step 0 : you need chrome for this. Also install modules :
# pip install selenium && pip install webdriver_manager && pip install tinydb
# # 

driver = webdriver.Chrome(ChromeDriverManager().install())
# ****Minimise window
driver.maximize_window()
# # ************open Flipkart*****************
driver.get("https://www.flipkart.com/")
# *********************Email***************************8
driver.find_element_by_class_name("_2IX_2-").send_keys("6201470183")
# ************Passoword********************
driver.find_element_by_xpath("//input[@type=\"password\"]").send_keys("ishaanu")
# ****************Submit Button**********************
driver.find_element_by_class_name("_1D1L_j").submit()
# *****************go to the specific email**********

driver.get("https://www.flipkart.com/sony-alpha-ilce-6000y-b-in5-mirrorless-camera-body-dual-lens-16-50-mm-55-210/p/itm7c7f3243ab5e5?pid=CAME7JYVSNMHNYHQ&lid=LSTCAME7JYVSNMHNYHQUJPHRB&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&fm=organic&iid=09cd1f58-3a71-48bd-b307-9b81765b29b1.CAME7JYVSNMHNYHQ.SEARCH&ppt=hp&ppn=homepage&ssid=xs4nwq5p340000001621677644869")
# clicking
driver.find_element_by_class_name("_1KOMV2").click()




