from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Testbase:

    driver = None

    @classmethod
    def get_webdriver(cls):
        if not cls.driver:
            cls.driver = cls.__create_local_driver()
        return cls.driver

    @classmethod
    def __create_local_driver(cls):
        driver = webdriver.Chrome()
        return driver

    @classmethod
    def load_url(cls, url=None):
            cls.driver.get(url)

    @classmethod
    def load_url_env(cls):
        # Implement your logic to load the URL from environment variables.
        pass

    @classmethod
    def close_driver(cls):
        cls.driver.quit()
        cls.driver = None

