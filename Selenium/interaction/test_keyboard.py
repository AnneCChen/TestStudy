from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestKeyboard:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly.wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_shift(self):
        """"
        1. visit https://ceshiren.com/
        2. click search
        3. input search content, at the same time, press 'shift'
        """
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.id, "search-button").click()
        ele = self.driver.find_elements(By.id, "search-term").send_keys("selenium")
        ActionChains(self.driver).key_down(Keys.SHIFT, ele)
