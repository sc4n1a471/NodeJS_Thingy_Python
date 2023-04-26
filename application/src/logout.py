import time

from selenium.webdriver.common.by import By

from application.data import settings
from application.data.xpaths import XPATHS

def logout():
    print("Logging out...")
    time.sleep(1)
    settings.driver.switch_to.default_content()
    settings.driver.switch_to.frame(2)
    settings.driver.find_element(By.XPATH, XPATHS.get('logout_button')).click()