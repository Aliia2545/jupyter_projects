from time import sleep
from selenium import webdriver
import sqlite3
conn = sqlite3.connect(R'C:\Users\aliya\PycharmProjects\data.db')
cursor = conn.cursor()
browser = webdriver.Chrome(r'C:\Users\aliya\OneDrive\Рабочий стол\my_python_codes\chromedriver_win32\chromedriver.exe')
email = "aliya.beiwenalieva@gmail.com"
password = "2545Alii@"





try:
    browser.get('https://datamasters.ru/aianddata')
    sleep(5)
    browser.get('https://api.datamasters.ru/auth/login')
    sleep(10)
    print('Authorization...')
    email_input = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/span/div[1]/span/div/input')
    sleep(8)
    password_input = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/span/div[2]/span/div/input')
    email_input.clear()
    password_input.clear()
    email_input.send_keys(email)
    sleep(3)
    password_input.send_keys(password)
    sleep(6)
    browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/span/div[4]/button').click()
    sleep(15)
    print('Authorization ended success!')
    try:
        print('Getting amount of tasks...')
        count_tasks = browser.find_element_by_css_selector(
            '#rec334451942 > div > div > div > main > main > div > div.task-count')
        tasks_count = count_tasks.text[13:]
        a = 1
        print('Get amount of tasks success!')
        for _ in range((int(tasks_count) // 10) + 1):
            sleep(15)
            print('Getting all tasks...')
            all_tasks = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div/div/div/main/main/div/div[3]/div[1]/div')
            all_tasks_list = all_tasks.text.split('\n')
            print('Get all tasks success!')
            for i in range(a, int(tasks_count) + 1):
                if str(i) in all_tasks_list and str(i + 1) in all_tasks_list:
                    task = all_tasks_list[all_tasks_list.index(f'{i}'):all_tasks_list.index(f'{i + 1}')]
                    print(f'Inserting task {i} in database...')
                    cursor.execute(
                        f"""INSERT INTO "tasks" ('заголовок', 'страна', 'регионы постановщики', 'рейтинг','международная') VALUES ('{task[1]}', '{task[3]}', '{task[4]}', '{task[5]}', '{task[6]}');""")
                    conn.commit()
                    print(f'Inserting task {i} in database success!')
                else:
                    task = all_tasks_list[all_tasks_list.index(f'{i}'):]
                    print(f'Inserting task {i} in database...')
                    cursor.execute(
                        f"""INSERT INTO "tasks" ('заголовок', 'страна', 'регионы постановщики', 'рейтинг','международная') VALUES ('{task[1]}', '{task[3]}', '{task[4]}', '{task[5]}', '{task[6]}');""")
                    conn.commit()
                    print(f'Inserting task {i} in database success!')
                    a += 10
                    break
            sleep(8)
            try:
                # print('Going to next page...')
                next_button = browser.find_element_by_xpath(
                    '/html/body/div[2]/div/div/div/div/main/main/div/div[3]/div[2]/div/div/a[2]').click()
            except Exception as ex:
                break
            sleep(10)
            print('Parsed Success!')
        print("Finish")
    except Exception as ex:
        browser.close()
        print(ex)
    sleep(3000)
    browser.close()
except Exception as ex:
    browser.quit()
    raise ex






