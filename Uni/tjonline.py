from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def fileread():
    f = open("myclass.conf", "r")
    print(f.read())
    

def checkdate():
    return

def main():
    browser = webdriver.Firefox()
    browser.get('http://lms13.iauec.ac.ir/index.php')

    userElem = browser.find_element_by_id('username')
    userElem.send_keys('')  # admn no here
    passwordElem = browser.find_element_by_id('password')
    passwordElem.send_keys('')  # password here
    loginElem = browser.find_element_by_class_name('submitBtn')
    loginElem.click()



if __name__ == '__main__':
    fileread()
    #checkdate()
    #main()
