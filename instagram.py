from time import sleep
from selenium import webdriver
browser = webdriver.Chrome(r'C:\Users\aliya\OneDrive\Рабочий стол\my_python_codes\chromedriver_win32\chromedriver.exe')
login = "aliya.beiwenalieva@gmail.com"
password = "Aliia65942545"
input_name = "ysl__s"

try:
    browser.get('https://www.instagram.com/')
    sleep(5)
    login_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
    sleep(5)
    password_input = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
    sleep(5)
    login_input.clear()
    password_input.clear()
    login_input.send_keys(login)
    sleep(5)
    password_input.send_keys(password)
    sleep(5)
    browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
    sleep(15)
    print('You entered successfully')
    search = browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    sleep(10)
    print('prepare to enter the name')
    # search.clear()
    search.send_keys(input_name)
    print('name was entered')
    sleep(5)
    click_search = browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
    print('account was found')
    sleep(5)
    browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div/div/div/div[1]/a/div[1]/div[2]').click()
    sleep(3)
    browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
    print('photo was liked')
    sleep(3)
    browser.find_element_by_xpath('/html/body/div[6]/div[3]/button').click()
    print('successfully exit')
    sleep(3)


    sleep(3000)
    browser.close()
except Exception as ex:
    browser.quit()
    raise ex


