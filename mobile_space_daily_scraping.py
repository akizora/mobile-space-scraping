from selenium import webdriver
import re
import csv
import sys
import time

def invoke_chrome_driver():
    options = webdriver.ChromeOptions()
    ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X)'
    ua += ' AppleWebKit/602.3.12 (KHTML, like Gecko)'
    ua += ' Version/10.0 Mobile/14C92 Safari/602.1'
    options.add_argument('--user-agent=%s' % ua)    
    chromedriver = "/Applications/chromedriver"
    # chromedriver = "C:\chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(chrome_options=options,executable_path=chromedriver)
    return driver

if __name__ == "__main__":
    print('start!!!')
    driver = invoke_chrome_driver()
    result_lists = []
    # スクレイピングするURLを記載する
    url = 'http://12.xmbs.jp/LACOWEGOUNI-44112-d2.php?guid=on'
    # どこまでのページを取得するか記載する
    page_num = 51
    
    for i in range(0, 51):
        # 日記一覧ページ取得
        if i == 0:
            driver.get(url)
        else:
            driver.get(url + '&page2=' + str(i))

        # 各日記のURLを取得する
        daily_url_list = []
        daily_url_elements = driver.find_elements_by_xpath('//font/a')
        for url_elem in daily_url_elements:
            daily_url = url_elem.get_attribute('href')
            daily_url_list.append(daily_url)
            # print(daily_url)
        
        for daily_url in daily_url_list:
            # daily_url_list.append(url_elem.get_attribute('href'))
            if daily_url is None:
                continue
            if 'action' in daily_url:
                continue
            # 日記ページにアクセス
            driver.get(daily_url)
            result_list = []
            try:
                html = driver.page_source
                html = html.replace('\n', '')

                # 投稿日時
                m_date = re.search(
                    r'<hr color="" width="95%" size="1" align="left">(.*?)<hr color="" width="95%" size="1" align="left">', 
                    html)
                daily_date = m_date.group(1)
                daily_date = daily_date.replace('<br>', '')
                result_list.append(daily_date)

                # 日記タイトル
                m_title = re.search(r'<font size="\+1">(.*?)<\/font>', html)
                daily_title = m_title.group(1)
                result_list.append(daily_title)

                # 投稿
                m_post = re.search(r'>編<\/a>\]<br>(.*?)ｺﾒﾝﾄする', html)
                daily_post_text = m_post.group(1)
                daily_post_text = daily_post_text.replace('<hr color="" width="95%" size="1" align="left">', '')
                daily_post_text = daily_post_text.replace('[<a href="LACOWEGOUNI-44112-d_resentry.php?guid=on&amp;action=res_com1&amp;n=', '')
                daily_post_text = daily_post_text.replace('<br>', '\n')

                result_list.append(daily_post_text)

                result_lists.append(result_list)
                # print(daily_post_text)
                # sys.exit()
            except Exception as e:
                print(e)
                print('取得できませんでした')
                pass

    path_w = './post_daily_data.csv'
    with open(path_w, mode='w') as f:
        writer = csv.writer(f)
        for result_list in result_lists:
            writer.writerow(result_list)
