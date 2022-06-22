from selenium import webdriver

driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
driver.get("https://www.amazon.com/")

searchbtn = driver.find_element_by_xpath("//input[@id='nav-search-submit-button']")
searchbtn.click()
