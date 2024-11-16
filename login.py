import time

from selenium import webdriver

driver = webdriver.Edge()

driver.get(f"https://www.vcg.com/creative-image/honglvdeng/")

time.sleep(30)
# 3WYV.29eUn!.nrN

driver.refresh()
print(driver.get_cookies())