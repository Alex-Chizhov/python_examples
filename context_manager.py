from selenium import webdriver
from colorama import Fore, Style


class ContextManager:

    def __init__(self):
        self.wd = webdriver.Chrome()

    def __enter__(self):
        self.wd.get("https://www.google.com/")
        return self.wd

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(Fore.RED + 'exc_type:', Style.RESET_ALL)
            print(exc_type)
            print(Fore.RED + 'exc_value:', Style.RESET_ALL)
            print(exc_val)
            print(Fore.RED + 'exc_traceback:',  Style.RESET_ALL)
            print(exc_tb)

        self.wd.quit()
        return True

with ContextManager() as browser:
    browser.find_element_by_xpath('//')