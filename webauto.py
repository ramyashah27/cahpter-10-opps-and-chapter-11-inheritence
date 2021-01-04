from selenium import webdriver
driver = webdriver.Chrome() 
# driver.get('https://youtube.com')
# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('HUSTYPLAYS')   
# searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
from selenium import webdriver
driver = webdriver.Chrome() 
driver.get('https://learn.byjus.com/login')
driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[2]/div[1]/div/div[2]/div[1]')
# searchbox.send_keys('HUSTYPLAYS')   
# searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')