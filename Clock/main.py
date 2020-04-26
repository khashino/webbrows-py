from selenium import webdriver
from selenium.webdriver.common.by import By

#https://www.selenium.dev/documentation/en/selenium_installation/installing_webdriver_binaries/
#https://www.selenium.dev/documentation/en/webdriver/web_element/

#https://selenium-python.readthedocs.io/locating-elements.html

def main():
    browser = webdriver.Firefox()
    browser.get('http://www.bonyansystem.com/hr/login.php')

    userElem = browser.find_element_by_name('username')
    userElem.send_keys('')  # admn no here
    passwordElem = browser.find_element_by_name('password')
    passwordElem.send_keys('')  # password here
    loginElem = browser.find_element(By.XPATH, '//button[text()="Login"]')
    loginElem.click()

    #loginElem = browser.find_element(By.XPATH, '//button[text()="Confirm"]')
    loginElem = browser.find_element(By.XPATH, '//button[text()="Clock"]')
    loginElem.click()

    file_data = []
    table = browser.find_elements_by_tag_name('tbody')[1]
    body_line = table.find_elements_by_tag_name('tr')
    for line in body_line:
        contents = line.find_element_by_tag_name('th')
        file_data.append(contents.text)
        #print(contents.text)
        contents = line.find_elements_by_tag_name('td')
        for content in contents:
            body_text = content.text
            file_data.append(body_text)
            #print(body_text)



    #4-9-14
    x = 4
    dayoff = []
    dayproblem = []
    karkard = []
    while x <= len(file_data):
        if str(file_data[x]) == '-':
            dayproblem.append(file_data[x-4])
        elif str(file_data[x]) == '':
            dayoff.append(file_data[x-4])
        else:
            karkard.append(file_data[x])
        x += 5
    print(karkard)

    totalmin = 0
    for tm in karkard:
        timeParts = [int(s) for s in tm.split(':')]
        totalmin += int(timeParts[0]) * 60 + int(timeParts[1])
    print("Total work Hour : "+str(totalmin)+" min | or "+str(totalmin/60)+" hour")
    print("#############################")
    print("Total Day off : "+str(len(dayoff)))
    print(dayoff)
    print("#############################")
    print("Total Day not set correctly : " + str(len(dayproblem)))
    print(dayproblem)

    loginElem = browser.find_element_by_link_text('Sign Out')
    loginElem.click()

    browser.close()
    #browser.quit()

if __name__ == '__main__':
    main()
