import sys
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TestMouse:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        # 
        self.driver.implicitly_wait(3)

    

    def __init__(self):
        self.setup_class()
    def teardown_class(self):
        self.driver.quit()



    def test_double_click(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        ele =  self.driver.find_element(By.ID,"primary_btn")
        ActionChains(self.driver).double_click(ele).perform()
        time.sleep(300)

# t1 = TestMouse()
# t1.test_double_click()

    def test_drap_and_drag(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
        start_ele  = self.driver.find_element(By.ID,"item1")
        target_ele = self.driver.find_element(By.ID,"item3")
        ActionChains(self.driver).drag_and_drop(start_ele,target_ele).perform()
        time.sleep(200)

        
# t1 = TestMouse()
# t1.test_drap_and_drag()

    def test_move_element(self):
       self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
       ele = self.driver.find_element(By.CSS_SELECTOR, ".menu")
       ActionChains(self.driver).move_to_element(ele).perform()
       time.sleep(300)

t1 = TestMouse()
t1.test_move_element() 