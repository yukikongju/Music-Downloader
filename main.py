#!/usr/bin/python

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def main():
    options = webdriver.ChromeOptions()
    #  options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #  driver = webdriver.Chrome(executable_path = r'C:\tools\driver\chromedriver.exe', options=options)
    driver = webdriver.Chrome()
    url = 'https://www.mp3juices.cc/'
    driver.get(url)

    try:
        search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'query')))
        search_bar.send_keys("mgk")
        search_bar.send_keys(Keys.ENTER)
        download_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, 'download')).click()
    except TimeoutException:
        print("Too much Time!")
    #  search_bar = driver.find_element_by_id("query")
    #  search_bar.send_keys("mgk")
    #  search_bar.submit()
    #  search_bar.send_keys(Keys.RETURN)
    #  download_button = driver.find_element_by_class_name("result")
    #  download_button = driver.find_element_by_id("result_1")
    #  search_bar.send_keys(Keys.ENTER)
    #  search_bar.send_keys(Keys.ESCAPE)
    #  search_bar.clear()
    #  download_button = driver.find_element_by_class_name("download 1")
    #  download_button.click()
    #  driver.close()

def mp3clan():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path = r'C:\tools\driver\chromedriver.exe', options=options)
    url = 'http://mp3clan.top/'
    driver.get(url)

    driver.implicitly_wait(10)
    search_bar = driver.find_element_by_class_name("searchClan-input-left")
    search_bar.send_keys("mgk")
    search_bar.send_keys(Keys.RETURN)
    #  search_bar.send_keys(Keys.ENTER)
    #  search_bar.send_keys(Keys.ESCAPE)
    #  search_bar.clear()
    #  download_button = driver.find_element_by_class_name("download 1")
    #  download_button.click()

def youtube():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path = r'C:\tools\driver\chromedriver.exe', options=options)
    url='https://music.youtube.com/playlist?list=PLzx7xtGqjNzoElKjq_zmpzgoS8RNrqHYh'
    #  url = "https://www.youtube.com/"
    driver.get(url)

    driver.implicitly_wait(10)
    playlist= driver.find_element_by_class_name("style-scope ytmusic-playlist-shelf-renderer")


if __name__ == "__main__":
    main()
    #  mp3clan()
    #  youtube()
