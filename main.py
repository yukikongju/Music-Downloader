import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome


def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path=r'C:\tools\driver\chromedriver.exe',
        options=options)
    #  url = "https://www.mp3juices.cc/"
    #  driver.get(url)


if __name__ == "__main__":
    main()
