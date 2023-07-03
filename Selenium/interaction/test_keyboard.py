import sys
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TestKeyboard:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        # 
        self.driver.implicitly_wait(3)

    def __init__(self):
        self.setup_class()
    def teardown_class(self):
        self.driver.quit()

    def test_shift(self):
        """"
        1. visit https://ceshiren.com/
        2. click search
        3. input search content, at the same time, press 'shift'
        """
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, "search-button").click()
        ele = self.driver.find_element(By.ID, "search-term")
        ActionChains(self.driver).key_down(Keys.SHIFT, ele).send_keys("selenium").perform()
        time.sleep(300)
        
# t1= TestKeyboard()
# t1.test_shift()

    def test_enter_by_sendkeys(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.ID,"APjFqb").send_keys("selenium")
        # 1st way
        # self.driver.find_element(By.ID,"APjFqb").send_keys(Keys.ENTER)
        # 2nd
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        time.sleep(300)

# t1 = TestKeyboard()
# t1.test_enter_by_sendkeys()


    def test_copy_and_paste(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.ID,"APjFqb").send_keys("selenium")
        command_control = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL 
        ActionChains(self.driver).key_down(Keys.SHIFT,ele).send_keys("Selenium!").key_down(Keys.ARROW_LEFT).key_down(command_control).send_keys("xvv").key_up(command_control).perform()
        time.sleep(300)

t1 = TestKeyboard()
t1.test_copy_and_paste()