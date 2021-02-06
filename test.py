from selenium import webdriver
import re
import csv
import time



import openpyxl



def invoke_chrome_driver():
    options = webdriver.ChromeOptions()
    ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X)'
    ua += ' AppleWebKit/602.3.12 (KHTML, like Gecko)'
    ua += ' Version/10.0 Mobile/14C92 Safari/602.1'
    options.add_argument('--user-agent=%s' % ua)    
    # chromedriver = "/Applications/chromedriver"
    chromedriver = "C:\chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(chrome_options=options,executable_path=chromedriver)
    return driver

if __name__ == "__main__":
    driver = invoke_chrome_driver()
    result_lists = []
    url_1 = 'https://www.yodobashi.com/'
    url_2 = 'https://www.toysrus.co.jp/s/dsg-670085300'
    url_3 = 'https://www.biccamera.com/bc/item/7477448/'

# https://www.yodobashi.com/product/100000001005291839/
# https://www.yodobashi.com/product/100000001005291839/

    workbook = openpyxl.load_workbook('test.xlsx')
    sheet = workbook["Sheet1"]

    time.sleep(5)
    for cols in sheet.iter_cols(min_row=2, min_col=2, max_row=7, max_col=2):
        for cell in cols:
            print(cell.value)
            word = cell.value
            driver.get(url_1)
            time.sleep(3)
            search_input = driver.find_element_by_id('getJsonData')
            search_input.send_keys(word)
            search_btn = driver.find_element_by_class_name('h-icnSrch')
            search_btn.click()
            time.sleep(30)

            


    # for i in range(0, page_num):
        # driver.get(url + '&disp=' + str(i))
        # html = driver.page_source
        # html = html.replace('\n', '')
        # m = re.search(r'<a name="viewlist"><\/a>(.*?)<font size=', html)
        # matched_html = m.group(1)
        # post_texts = matched_html.split('<hr color="#C0C0C0" width="95%" size="1" align="left">')
        # for post in post_texts:
        #     try:
        #         print('test')
        #     except Exception as e:
        #         print(e)
        #         print('取得できませんでした')
        #         pass



    # path_w = './post_data.csv'
    # with open(path_w, mode='w') as f:
    #     writer = csv.writer(f)
    #     for result_list in result_lists:
    #         writer.writerow(result_list)
