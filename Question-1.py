from time import sleep   #Import sleep to pause execution for some seconds
from selenium.webdriver import Chrome,ChromeOptions  #Import Chrome browser driver and Chrome options
from selenium.webdriver.common.by import By  #Import By class to locate elements using different locators
from selenium.webdriver.support.wait import WebDriverWait #Import explicit wait
from selenium.webdriver.support import expected_conditions as EC #Import the conditions for explicit waits
o=ChromeOptions()  #Chrome browser options
o.add_experimental_option("detach",True) #Keep the browser open even after script execution gets completed
driver=Chrome(options=o)#Launching the Chrome browser with custom option
driver.implicitly_wait(10)#Import implicit wait
driver.get("https://www.shoppersstack.com/")#open the shopperstack website
driver.maximize_window()#to maximize the window
driver.find_element(By.XPATH,"//img[@src='https://m.media-amazon.com/images/I/61BGE6iu4AL._AC_UY218_.jpg']").click()#locating the particular apple category product using x path locator and clicking it
driver.find_element(By.ID,"Check Delivery").send_keys("302017") #Locating the delivery input field and entering the pincode
sleep(5)#pausing the execution for 5 seconds
wait=WebDriverWait(driver,10)#Create explicit wait object with 10 second wait time
wait.until(EC.presence_of_element_located((By.ID,"Check")))#wait until the presence of check button
btn=driver.find_element(By.ID,"Check")#locate the check button
btn.click()#click the check button
sleep(4)#pausing execution for 4 seconds
driver.quit()#quitting the browser



