# from time import sleep
# from selenium import webdriver
# import sqlite3
#
# conn = sqlite3.connect('')
# cursor = conn.cursor()
#
# browser = webdriver.Chrome(r'C:\Users\aliya\OneDrive\Рабочий стол\my_python_codes\chromedriver_win32\chromedriver.exe')
#
# try:
#     browser.get('https://pogoda.turtella.ru/kyrgyzstan/jalal-abad/archive')
#     sleep(5)
#     items = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]')
#     all_data = items.text.split('\n')
#     all_data2 = all_data[:-37]
#     for i in all_data2:
#         res = i.split(' ')
#
#         print(res)


    # a = 0
    # for i in range(27):
    #     browser.get(
    #         f'http://www.energo-es.kg/ru/o-kompanii/obem-vody-v-toktogulskom-vodokhranilishche?start={a}')
    #
    #     # count_items = browser.find_element_by_xpath(
    #     #             '/html/body/main/div/div[1]/div/article/div/nav/ul/li[1]/div')
    #     # total_item = count_items.text[10:]
    #     sleep(10)
    #     all_data = browser.find_element_by_xpath('/html/body/main/div/div[1]/div/article/div')
    #     sleep(10)
    #     cutted = all_data.text.split('\n')
    #     cutted2 = cutted[4:34]
    #     for feature in cutted2:
    #         res_f = feature.split(' ')
    #         # print(res_f[0])
    #         cursor.execute(
    #             f"""INSERT INTO "hydroelectric_power_station" ('date', 'average_daily_flow_m3/s', 'average_daily_consumption_m3/s', 'water_volume_billion.m3') VALUES ('{res_f[0]}', '{res_f[1]}', '{res_f[2]}', '{res_f[3]}');""")
    #         conn.commit()
    #     sleep(10)
    #     a += 30



#     sleep(4000)
#     browser.quit()
# except Exception as ex:
#     browser.quit()
#     raise ex


from time import sleep
from selenium import webdriver
import sqlite3
conn = sqlite3.connect('db_toktogul.db')
cursor = conn.cursor()

august_2021 = """
1 31% - 36.5°C 22.0°C 4 м/с
2 15% - 36.0°C 24.5°C 3 м/с
3 34% - 36.5°C 19.5°C 4 м/с
4 11% - 37.5°C 19.5°C 4 м/с
5 18% - 36.0°C 19.5°C 4 м/с
6 6% - 35.5°C 19.0°C 4 м/с
7 35% - 35.5°C 17.5°C 3 м/с
8 15% - 36.5°C 20.0°C 3 м/с
9 0% - 37.5°C 20.5°C 4 м/с
10 0% - 35.5°C 18.5°C 3 м/с
11 1% - 36.5°C 18.5°C 3 м/с
12 5% - 36.0°C 19.5°C 4 м/с
13 35% - 34.0°C 18.5°C 4 м/с
14 35% 1 м.м. 30.5°C 17.5°C 3 м/с
15 16% - 29.5°C 19.0°C 3 м/с
16 1% - 30.0°C 16.7°C 3 м/с
"""

july_2021 = """
1 19% - 36.5°C 22.0°C 4 м/с
2 33% - 33.5°C 22.0°C 4 м/с
3 21% - 37.0°C 20.5°C 4 м/с
4 1% - 38.5°C 21.0°C 4 м/с
5 5% - 40.0°C 21.5°C 4 м/с
6 23% - 39.0°C 23.0°C 3 м/с
7 1% - 39.5°C 22.5°C 3 м/с
8 0% - 40.5°C 24.0°C 3 м/с
9 2% - 41.0°C 25.5°C 4 м/с
10 48% 3 м.м. 35.0°C 24.5°C 4 м/с
11 14% - 34.5°C 20.5°C 4 м/с
12 79% 18 м.м. 28.0°C 15.5°C 2 м/с
13 61% 5 м.м. 28.5°C 18.5°C 3 м/с
14 38% 1 м.м. 33.0°C 17.0°C 3 м/с
15 26% - 34.0°C 20.5°C 3 м/с
16 49% 2 м.м. 26.5°C 19.5°C 3 м/с
17 47% 2 м.м. 27.0°C 15.0°C 2 м/с
18 61% 1 м.м. 29.5°C 20.0°C 2 м/с
19 11% - 33.5°C 19.5°C 3 м/с
20 37% 1 м.м. 34.5°C 20.5°C 3 м/с
21 9% - 32.5°C 20.5°C 3 м/с
22 2% - 34.5°C 21.0°C 3 м/с
23 7% - 37.0°C 20.0°C 3 м/с
24 1% - 39.5°C 24.0°C 3 м/с
25 0% - 42.0°C 25.0°C 3 м/с
26 0% - 41.5°C 24.5°C 3 м/с
27 4% - 38.5°C 24.0°C 3 м/с
28 5% - 37.0°C 24.5°C 3 м/с
29 36% - 37.0°C 23.5°C 4 м/с
30 9% - 34.0°C 22.5°C 3 м/с
31 20% - 36.5°C 21.5°C 3 м/с
"""

june_2021 = """
1 2% - 34.0°C 17.5°C 3 м/с
2 3% - 35.0°C 17.0°C 3 м/с
3 2% - 35.0°C 17.5°C 4 м/с
4 45% 1 м.м. 34.5°C 19.5°C 3 м/с
5 7% - 37.5°C 19.0°C 4 м/с
6 7% - 37.5°C 21.0°C 4 м/с
7 44% - 36.5°C 20.5°C 4 м/с
8 56% 1 м.м. 29.5°C 17.5°C 4 м/с
9 47% - 32.5°C 17.0°C 3 м/с
10 27% 5 м.м. 31.5°C 16.5°C 3 м/с
11 3% - 32.5°C 17.5°C 4 м/с
12 41% 1 м.м. 31.5°C 16.5°C 4 м/с
13 38% 1 м.м. 30.0°C 15.0°C 5 м/с
14 24% 2 м.м. 30.0°C 14.5°C 4 м/с
15 48% 1 м.м. 29.5°C 14.0°C 4 м/с
16 0% - 31.5°C 13.5°C 3 м/с
17 2% - 33.0°C 14.0°C 3 м/с
18 20% - 33.5°C 16.5°C 4 м/с
19 9% - 33.0°C 15.5°C 4 м/с
20 1% - 32.0°C 16.0°C 4 м/с
21 0% - 33.0°C 14.5°C 4 м/с
22 10% - 32.5°C 14.0°C 4 м/с
23 1% - 32.0°C 15.5°C 3 м/с
24 0% - 33.5°C 15.5°C 4 м/с
25 3% - 33.0°C 15.5°C 5 м/с
26 1% - 32.0°C 15.0°C 4 м/с
27 1% - 35.5°C 16.0°C 3 м/с
28 6% - 37.5°C 18.5°C 3 м/с
29 17% - 37.5°C 19.0°C 3 м/с
30 16% - 37.5°C 19.0°C 4 м/с
"""

may_2021 = """

1 20% - 26.5°C 15.0°C 1 м/с
2 23% 3 м.м. 27.0°C 13.5°C 2 м/с
3 10% - 29.0°C 16.0°C 2 м/с
4 9% - 31.0°C 15.5°C 3 м/с
5 10% - 29.5°C 17.5°C 3 м/с
6 59% 2 м.м. 23.5°C 17.5°C 2 м/с
7 31% - 25.0°C 14.5°C 1 м/с
8 30% - 27.0°C 15.0°C 3 м/с
9 45% 1 м.м. 27.5°C 14.5°C 3 м/с
10 16% - 27.0°C 16.5°C 2 м/с
11 80% 3 м.м. 20.0°C 17.0°C 2 м/с
12 22% 1 м.м. 24.5°C 13.0°C 2 м/с
13 17% - 25.5°C 10.0°C 2 м/с
14 3% - 25.5°C 10.5°C 2 м/с
15 23% 4 м.м. 25.5°C 8.5°C 3 м/с
16 52% 2 м.м. 27.5°C 10.5°C 2 м/с
17 0% - 28.5°C 11.5°C 3 м/с
18 6% - 29.5°C 12.5°C 3 м/с
19 35% - 27.5°C 15.5°C 3 м/с
20 7% - 28.0°C 13.0°C 3 м/с
21 43% 1 м.м. 26.5°C 11.5°C 2 м/с
22 15% 1 м.м. 28.0°C 12.0°C 3 м/с
23 33% - 28.5°C 12.5°C 3 м/с
24 63% 1 м.м. 27.5°C 14.0°C 3 м/с
25 16% - 28.5°C 13.5°C 3 м/с
26 7% - 30.0°C 17.0°C 2 м/с
27 13% - 31.5°C 17.0°C 3 м/с
28 1% - 33.5°C 17.5°C 3 м/с
29 5% - 34.0°C 18.0°C 2 м/с
30 26% 1 м.м. 32.5°C 17.0°C 3 м/с
31 25% 1 м.м. 32.5°C 16.5°C 3 м/с
"""

april_2021 = """
1 80% 14 м.м. 5.0°C 3.0°C 2 м/с
2 2% - 9.5°C -3.0°C 3 м/с
3 7% - 15.0°C 1.0°C 3 м/с
4 44% - 14.5°C 6.0°C 2 м/с
5 77% 11 м.м. 10.5°C 4.5°C 2 м/с
6 8% - 14.5°C 3.0°C 2 м/с
7 41% - 15.0°C 7.0°C 2 м/с
8 3% - 19.5°C 4.5°C 2 м/с
9 17% - 19.5°C 5.5°C 3 м/с
10 0% - 22.0°C 5.5°C 3 м/с
11 7% - 21.5°C 7.0°C 2 м/с
12 4% - 20.5°C 7.5°C 1 м/с
13 48% - 18.5°C 10.5°C 2 м/с
14 13% - 21.5°C 8.5°C 2 м/с
15 25% - 22.5°C 11.0°C 2 м/с
16 36% - 22.0°C 11.0°C 2 м/с
17 7% - 22.0°C 10.0°C 2 м/с
18 48% - 19.0°C 10.0°C 3 м/с
19 14% - 21.5°C 9.0°C 2 м/с
20 26% - 21.5°C 11.0°C 3 м/с
21 83% 40 м.м. 10.5°C 9.0°C 2 м/с
22 49% 2 м.м. 15.5°C 5.5°C 2 м/с
23 9% - 20.5°C 7.0°C 2 м/с
24 18% - 22.0°C 8.5°C 2 м/с
25 11% - 25.0°C 9.0°C 2 м/с
26 1% - 27.5°C 10.5°C 2 м/с
27 0% - 28.0°C 11.0°C 3 м/с
28 0% - 29.0°C 15.0°C 3 м/с
29 0% - 31.5°C 14.5°C 2 м/с
30 16% - 30.5°C 15.0°C 2 м/с
"""

march_2021 = """
1 5% - 7.0°C -4.5°C 3 м/с
2 69% - 9.0°C 1.5°C 2 м/с
3 92% 6 м.м. 4.5°C 4.5°C 2 м/с
4 49% - 9.5°C 3.0°C 2 м/с
5 55% 5 м.м. 7.5°C 5.0°C 3 м/с
6 48% - 9.5°C 0.0°C 3 м/с
7 47% - 9.0°C 3.0°C 2 м/с
8 22% - 9.0°C 4.0°C 2 м/с
9 55% - 13.0°C 5.0°C 2 м/с
10 78% 3 м.м. 11.5°C 7.0°C 2 м/с
11 74% 14 м.м. 6.5°C 7.0°C 2 м/с
12 33% - 13.5°C 4.0°C 2 м/с
13 33% - 16.0°C 9.0°C 1 м/с
14 90% 16 м.м. 3.5°C 9.5°C 2 м/с
15 77% - 4.5°C 0.0°C 2 м/с
16 32% - 8.5°C 2.5°C 1 м/с
17 98% 5 м.м. 3.5°C 2.5°C 1 м/с
18 24% - 12.0°C 0.5°C 4 м/с
19 34% - 14.0°C 2.5°C 5 м/с
20 29% - 17.0°C 5.5°C 4 м/с
21 63% 19 м.м. 9.5°C 7.5°C 3 м/с
22 60% - 14.5°C 6.0°C 3 м/с
23 51% - 17.0°C 8.0°C 2 м/с
24 16% - 18.5°C 6.0°C 3 м/с
25 32% - 18.5°C 8.0°C 3 м/с
26 76% 24 м.м. 14.0°C 12.0°C 4 м/с
27 35% 3 м.м. 18.5°C 9.5°C 2 м/с
28 86% 33 м.м. 11.5°C 10.0°C 3 м/с
29 79% 22 м.м. 8.0°C 7.5°C 3 м/с
30 72% 4 м.м. 7.5°C 4.0°C 2 м/с
31 20% - 11.5°C 3.0°C 2 м/с
"""

februry_2021 = """
1 42% - 4.5°C -1.5°C 3 м/с
2 25% - 5.0°C 0.0°C 2 м/с
3 0% - 3.0°C -3.0°C 4 м/с
4 5% - 3.0°C -4.5°C 4 м/с
5 55% - 3.5°C -4.0°C 3 м/с
6 76% - 6.5°C -1.0°C 3 м/с
7 97% 1 м.м. 7.0°C 4.0°C 2 м/с
8 60% - 8.5°C 3.5°C 1 м/с
9 92% 10 м.м. 8.0°C 3.0°C 2 м/с
10 90% - 10.0°C 3.5°C 2 м/с
11 49% - 11.0°C 3.5°C 2 м/с
12 36% - 11.0°C 2.5°C 3 м/с
13 69% - 10.5°C 2.5°C 3 м/с
14 13% - 13.5°C 6.5°C 2 м/с
15 20% - 12.5°C 3.5°C 4 м/с
16 40% - 11.5°C 3.5°C 4 м/с
17 0% - 12.5°C 3.5°C 4 м/с
18 19% - 14.0°C 4.5°C 4 м/с
19 48% - 15.5°C 5.5°C 3 м/с
20 85% 6 м.м. 8.5°C 8.0°C 2 м/с
21 93% 15 м.м. 6.0°C 6.5°C 1 м/с
22 78% 8 м.м. 8.0°C 6.0°C 1 м/с
23 78% 2 м.м. 7.5°C 3.5°C 2 м/с
24 80% 3 м.м. 4.5°C 4.5°C 1 м/с
25 89% 19 м.м. -5.0°C -2.0°C 3 м/с
26 20% - -2.0°C -7.0°C 1 м/с
27 59% - 0.0°C -7.0°C 2 м/с
28 1% - 3.0°C -6.5°C 2 м/с
"""

january_2021 = """
1 4% - -0.5°C -7.5°C 2 м/с
2 0% - -1.5°C -9.5°C 3 м/с
3 1% - 0.5°C -8.5°C 3 м/с
4 0% - 0.5°C -7.5°C 3 м/с
5 34% - -2.0°C -8.0°C 2 м/с
6 51% - -4.0°C -7.5°C 1 м/с
7 74% - -4.0°C -8.0°C 1 м/с
8 14% - -4.5°C -10.5°C 1 м/с
9 0% - -6.0°C -13.0°C 3 м/с
10 0% - -3.5°C -11.5°C 4 м/с
11 0% - -0.5°C -9.0°C 4 м/с
12 25% - 3.5°C -4.0°C 2 м/с
13 91% 1 м.м. 3.5°C 1.0°C 1 м/с
14 7% - 3.5°C -1.5°C 1 м/с
15 0% - 6.0°C -1.0°C 3 м/с
16 0% - 8.0°C 0.0°C 4 м/с
17 6% - 7.0°C -1.5°C 4 м/с
18 23% - 7.0°C -1.5°C 3 м/с
19 70% - 8.5°C 3.5°C 3 м/с
20 59% 2 м.м. 9.0°C 3.5°C 3 м/с
21 6% - 7.0°C 1.5°C 3 м/с
22 98% 20 м.м. -2.5°C 2.0°C 2 м/с
23 86% 1 м.м. -4.0°C -8.5°C 1 м/с
24 44% - -2.5°C -8.0°C 2 м/с
25 42% - -1.0°C -9.5°C 2 м/с
26 9% - 0.5°C -7.5°C 3 м/с
27 14% - 0.0°C -8.0°C 3 м/с
28 0% - 0.0°C -8.0°C 3 м/с
29 0% - -0.5°C -8.0°C 4 м/с
30 4% - 1.0°C -7.0°C 5 м/с
31 35% - 3.5°C -2.0°C 4 м/с
"""

december_2020 = """
1 96% 1 м.м. 2.5°C -0.5°C 2 м/с
2 63% - 4.5°C 0.5°C 1 м/с
3 88% 9 м.м. 5.0°C 1.5°C 1 м/с
4 100% 24 м.м. 3.5°C 4.0°C 1 м/с
5 76% 9 м.м. 2.5°C 1.0°C 1 м/с
6 38% - 1.5°C -2.0°C 1 м/с
7 72% - 2.5°C -2.0°C 1 м/с
8 61% - 2.5°C -1.5°C 1 м/с
9 60% - 2.0°C -2.0°C 1 м/с
10 31% - 2.5°C -2.0°C 1 м/с
11 21% - 3.5°C -1.0°C 1 м/с
12 24% - 2.5°C -2.0°C 2 м/с
13 36% - 2.5°C -2.5°C 2 м/с
14 54% - 0.5°C -3.0°C 2 м/с
15 78% - 0.0°C -4.5°C 2 м/с
16 40% - 1.0°C -6.0°C 2 м/с
17 1% - 1.0°C -4.5°C 3 м/с
18 16% - 0.0°C -5.0°C 4 м/с
19 70% - 1.5°C -5.0°C 3 м/с
20 76% 2 м.м. 2.5°C -0.5°C 1 м/с
21 75% 2 м.м. 1.5°C -2.5°C 1 м/с
22 60% - 2.5°C -4.0°C 2 м/с
23 46% - 2.5°C -3.5°C 2 м/с
24 41% - 3.0°C -3.0°C 2 м/с
25 59% - 3.5°C 0.0°C 3 м/с
26 62% - 3.0°C 0.5°C 1 м/с
27 100% 3 м.м. 0.5°C -2.0°C 1 м/с
28 47% 1 м.м. -2.5°C -6.0°C 1 м/с
29 13% - -1.5°C -9.5°C 1 м/с
30 2% - 0.5°C -8.0°C 1 м/с
31 0% - -0.5°C -7.5°C 2 м/с
"""

november_2020 = """
1 6% - 20.0°C 5.5°C 2 м/с
2 35% - 19.5°C 7.5°C 2 м/с
3 0% - 20.5°C 7.0°C 2 м/с
4 1% - 18.5°C 8.0°C 2 м/с
5 0% - 21.0°C 5.5°C 2 м/с
6 0% - 19.5°C 7.0°C 2 м/с
7 40% - 21.0°C 10.0°C 2 м/с
8 54% - 23.0°C 12.5°C 2 м/с
9 45% - 11.5°C 10.5°C 1 м/с
10 9% - 13.5°C 4.5°C 1 м/с
11 68% - 14.0°C 6.5°C 1 м/с
12 79% 8 м.м. 8.5°C 9.0°C 1 м/с
13 85% 22 м.м. 8.5°C 7.0°C 2 м/с
14 100% 8 м.м. 4.5°C 5.0°C 1 м/с
15 20% - 7.0°C 2.0°C 1 м/с
16 7% - 7.5°C 2.0°C 1 м/с
17 46% - 5.5°C 2.5°C 1 м/с
18 100% 1 м.м. 4.5°C 1.5°C 1 м/с
19 77% 9 м.м. -3.0°C -1.5°C 2 м/с
20 6% - -2.5°C -7.5°C 1 м/с
21 5% - -1.5°C -8.0°C 1 м/с
22 75% - -2.5°C -6.5°C 1 м/с
23 33% 1 м.м. 1.0°C -4.0°C 2 м/с
24 22% - 0.0°C -6.5°C 1 м/с
25 52% - 1.5°C -4.5°C 1 м/с
26 56% - 2.5°C -4.0°C 2 м/с
27 79% - 5.0°C 1.0°C 1 м/с
28 84% 7 м.м. 1.5°C 2.0°C 2 м/с
29 10% - 2.0°C -2.5°C 1 м/с
30 40% - 1.0°C -4.0°C 1 м/с
"""

october_2020 = """
1 10% - 20.0°C 9.0°C 2 м/с
2 23% - 21.5°C 12.0°C 2 м/с
3 7% - 21.5°C 12.0°C 2 м/с
4 7% - 22.0°C 9.5°C 2 м/с
5 19% - 22.0°C 12.5°C 2 м/с
6 83% - 17.5°C 13.0°C 2 м/с
7 17% - 21.0°C 10.0°C 2 м/с
8 79% 1 м.м. 20.0°C 12.5°C 3 м/с
9 87% 5 м.м. 11.0°C 10.5°C 2 м/с
10 73% 1 м.м. 11.0°C 9.0°C 1 м/с
11 39% - 15.0°C 9.5°C 1 м/с
12 17% - 17.0°C 9.0°C 1 м/с
13 7% - 18.0°C 9.0°C 2 м/с
14 2% - 19.5°C 10.0°C 2 м/с
15 1% - 21.5°C 10.0°C 2 м/с
16 0% - 23.5°C 10.5°C 2 м/с
17 6% - 21.5°C 11.0°C 2 м/с
18 1% - 23.0°C 11.0°C 2 м/с
19 0% - 26.5°C 10.5°C 3 м/с
20 0% - 25.5°C 10.5°C 2 м/с
21 0% - 24.0°C 13.5°C 2 м/с
22 56% - 19.0°C 12.5°C 2 м/с
23 83% 8 м.м. 8.0°C 6.5°C 3 м/с
24 17% - 14.0°C 5.5°C 2 м/с
25 31% - 15.5°C 6.0°C 1 м/с
26 38% - 18.5°C 6.0°C 2 м/с
27 3% - 21.5°C 8.0°C 2 м/с
28 85% 1 м.м. 14.5°C 9.5°C 1 м/с
29 19% - 12.5°C 5.5°C 1 м/с
30 0% - 17.0°C 4.5°C 2 м/с
31 0% - 19.5°C 4.0°C 2 м/с
"""

september_2020 = """
1 10% - 29.5°C 18.5°C 2 м/с
2 8% - 31.0°C 19.5°C 3 м/с
3 62% 1 м.м. 24.0°C 20.0°C 3 м/с
4 2% - 28.5°C 17.0°C 3 м/с
5 1% - 30.0°C 18.5°C 3 м/с
6 16% - 28.5°C 19.0°C 3 м/с
7 1% - 25.5°C 15.5°C 2 м/с
8 4% - 26.5°C 16.5°C 2 м/с
9 2% - 27.5°C 17.0°C 2 м/с
10 3% - 29.0°C 17.0°C 3 м/с
11 2% - 30.5°C 17.0°C 3 м/с
12 1% - 29.0°C 17.0°C 3 м/с
13 0% - 29.0°C 15.0°C 3 м/с
14 7% - 29.5°C 17.5°C 3 м/с
15 7% - 29.0°C 16.5°C 3 м/с
16 1% - 29.0°C 17.0°C 2 м/с
17 6% - 27.0°C 16.5°C 3 м/с
18 49% - 22.0°C 13.0°C 4 м/с
19 15% - 21.0°C 11.0°C 2 м/с
20 0% - 27.0°C 12.0°C 3 м/с
21 0% - 28.5°C 14.5°C 3 м/с
22 12% - 26.0°C 15.5°C 3 м/с
23 17% - 23.0°C 14.5°C 2 м/с
24 1% - 24.5°C 12.5°C 2 м/с
25 0% - 25.5°C 12.0°C 3 м/с
26 10% - 24.5°C 11.5°C 2 м/с
27 34% - 25.0°C 14.5°C 2 м/с
28 24% - 24.5°C 13.5°C 2 м/с
29 42% - 22.5°C 14.0°C 2 м/с
30 38% - 16.5°C 10.0°C 2 м/с
"""

august_2020 = """
1 49% 2 м.м. 30.5°C 19.5°C 3 м/с
2 48% 1 м.м. 30.0°C 18.5°C 3 м/с
3 3% - 32.5°C 22.5°C 3 м/с
4 2% - 33.0°C 21.5°C 3 м/с
5 6% - 33.5°C 22.0°C 2 м/с
6 2% - 35.5°C 22.5°C 3 м/с
7 2% - 35.0°C 24.0°C 3 м/с
8 12% - 35.0°C 23.5°C 3 м/с
9 56% 2 м.м. 30.0°C 22.0°C 2 м/с
10 29% - 31.5°C 21.5°C 3 м/с
11 4% - 32.5°C 23.5°C 3 м/с
12 10% - 32.0°C 21.0°C 3 м/с
13 16% - 31.5°C 23.0°C 5 м/с
14 12% - 31.5°C 21.5°C 3 м/с
15 1% - 33.0°C 22.5°C 3 м/с
16 10% - 34.5°C 21.5°C 3 м/с
17 24% - 34.5°C 23.5°C 3 м/с
18 68% 5 м.м. 19.5°C 21.0°C 2 м/с
19 39% 1 м.м. 26.0°C 16.5°C 2 м/с
20 31% - 29.0°C 19.5°C 3 м/с
21 5% - 29.5°C 21.0°C 3 м/с
22 0% - 32.0°C 20.0°C 3 м/с
23 0% - 35.0°C 20.5°C 2 м/с
24 3% - 38.0°C 22.5°C 4 м/с
25 11% - 31.0°C 22.0°C 3 м/с
26 52% 3 м.м. 26.0°C 19.5°C 4 м/с
27 52% - 23.5°C 17.0°C 1 м/с
28 1% - 28.0°C 17.5°C 2 м/с
29 6% - 30.0°C 18.5°C 3 м/с
30 4% - 31.0°C 20.5°C 2 м/с
31 9% - 30.5°C 20.0°C 4 м/с
"""

weather_data_from_2020_august_to_2021_august = (
    august_2020, september_2020, october_2020, november_2020, december_2020, january_2021, februry_2021, march_2021,
    april_2021, may_2021, june_2021, july_2021, august_2021)


def cleaning_weather_data(weather_data):
    weather_data = weather_data.replace('\n', '')
    weather_data = weather_data.replace('м.м.', '')
    weather_data = weather_data.replace('°C', '')
    weather_data = weather_data.replace('м/с', '')
    weather_data = weather_data.replace('%', '')
    weather_data = weather_data.split(' ')
    for i in weather_data:
        if len(i) > 0:
            pass
        else:
            weather_data.remove(i)
    return tuple(weather_data[i:i + 6] for i in range(0, int(len(weather_data)), 6))


try:
    cleaned_weather_data = tuple(cleaning_weather_data(weather) for weather in weather_data_from_2020_august_to_2021_august)
    datas = {'2020.08': cleaned_weather_data[0],
             '2020.09': cleaned_weather_data[1],
             '2020.10': cleaned_weather_data[2],
             '2020.11': cleaned_weather_data[3],
             '2020.12': cleaned_weather_data[4],
             '2021.01': cleaned_weather_data[5],
             '2021.02': cleaned_weather_data[6],
             '2021.03': cleaned_weather_data[7],
             '2021.04': cleaned_weather_data[8],
             '2021.05': cleaned_weather_data[9],
             '2021.06': cleaned_weather_data[10],
             '2021.07': cleaned_weather_data[11],
             '2021.08': cleaned_weather_data[12]}
    for dates in datas.keys():
        for weather_data in datas.get(dates):