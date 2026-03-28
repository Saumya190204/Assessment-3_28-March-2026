from time import sleep #import sleep to pause execution for some seconds
from selenium.webdriver import Chrome,ChromeOptions #import Chrome browser driver and Chrome options
from selenium.webdriver.common.by import By #import By class to locate elements using different locators
from selenium.webdriver.common.action_chains import ActionChains #Import ActionChains for different actions
o=ChromeOptions() #Chrome browser options
o.add_experimental_option("detach",True)#Keep the browser open even after script execution gets completed
o.add_argument("--disable-notifications") # to disable browser notifications
driver=Chrome(options=o)#Launching the Chrome browser with custom option
driver.implicitly_wait(10)#importing implicit wait
driver.get("https://www.myntra.com/")#opening the myntra website
driver.maximize_window()#to maximize the browser window
actions=ActionChains(driver)#Create ActionChains object
genz=driver.find_element(By.XPATH,"//a[text()='Genz']")#locating the genz element
actions.move_to_element(genz).perform()#mouse hover on genz
jacket=driver.find_element(By.XPATH,"//a[text()='Jackets Under ₹899']")#finding Jackets Under ₹899
actions.click(jacket).perform()#clicking Jackets Under ₹899
sleep(4)#pausing execution for 4 seconds
brand=driver.find_element(By.XPATH,"(//div[@class='common-checkboxIndicator'])[14]")#finding the brand category
actions.click(brand).perform()#clicking the brand required
sleep(4)#pausing execution for 4 seconds
colour=driver.find_element(By.XPATH,"(//div[@class='common-checkboxIndicator'])[20]")#locating the required colour
actions.click(colour).perform()#selecting the required colour
sleep(4)#pausing execution for 4 seconds
dropdown=driver.find_element(By.XPATH,"//div[@class='sort-sortBy']")#locating the sortby dropdown
actions.move_to_element(dropdown).perform()#hover over the sort by dropdown
popularity=driver.find_element(By.XPATH,"(//label[@class='sort-label '])[3]")#loacting the popularity dropdown
actions.click(popularity).perform()#from sort by dropdown selecting popularity
sleep(2)#pausing execution for 2 seconds
product=driver.find_element(By.XPATH,"//a[@href='jackets/kashianxstyle/kashianxstyle-women-crop-denim-jacket/39201475/buy']")#loacting the product to buy
actions.click(product).perform()#clicking the product to buy
sleep(2)#pausing execution for 2 seconds
driver.switch_to.window(driver.window_handles[1])#switching the window handle
driver.find_element(By.XPATH,"//button[@class='size-buttons-size-button size-buttons-size-button-default']").click()#locating and clicking the size element
add=driver.find_element(By.XPATH,"//div[text()='ADD TO BAG']")#locating the add to bag button
actions.click(add).perform()#clciking the add to bag button
driver.quit()#quitting the browser




