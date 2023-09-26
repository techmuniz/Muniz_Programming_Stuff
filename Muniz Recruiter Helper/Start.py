'''from selenium import webdriver
from selenium.webdriver.common.by import By  # Importe a classe By corretamente
import time

driver = webdriver.Chrome()

folder = driver.find_element(By.id, 'ember2848')

time.sleep(1000)''''''


# //span [@id = 'ember2848']'''



'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.selenium.dev/pt-br/documentation/webdriver/elements/finders/')
driver.switch_to.window(driver.window_handles[0])

elemento = driver.find_element(By.XPATH, '//*[@id="m-pt-brdocumentationwebdriverdrivers"]').click()


time.sleep(1000)'''


