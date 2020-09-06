from selenium import webdriver
import re
import csv

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
    driver = invoke_chrome_driver()
    result_lists = []
    # スクレイピングするURLを記載する
    url = 'http://12.xmbs.jp/LACOWEGOUNI-**************-rl.php?guid=on'
    # どこまでのページを取得するか記載する
    page_num = 500
    for i in range(0, page_num):
        if i == 0:
            driver.get(url)
        else:
            driver.get(url + '&disp=' + str(i))
        html = driver.page_source
        html = html.replace('\n', '')
        m = re.search(r'<a name="viewlist"><\/a>(.*?)<font size=', html)
        matched_html = m.group(1)
        post_texts = matched_html.split('<br><br><hr color="#C0C0C0" width="95%" size="1" align="left">')
        for post in post_texts:
            result_list = []
            if post == '':
                continue
            try:
                # 投稿ID
                m_no = re.search(r'(.*?):', post)
                post_no = m_no.group(1)
                result_list.append(post_no)

                # 投稿者
                m_author = re.search(r':(.*?) ', post)
                post_author = m_author.group(1)
                result_list.append(post_author)

                # 投稿日時
                m_date = re.search(r' (.*?) ', post)
                post_date = m_date.group(1)
                result_list.append(post_date)

                # 投稿時間
                m_date = re.search(r'\) (.*?) ', post)
                post_time = m_date.group(1)
                result_list.append(post_time)

                # デバイス
                m_device = re.search(r':\d{2} (.*?)<br>', post)
                post_device = m_device.group(1)
                result_list.append(post_device)
                
                # 投稿
                m_post = re.search(r'<br>(.*)', post)
                post_text = m_post.group(1)
                result_list.append(post_text)
                result_lists.append(result_list)
            except Exception as e:
                print(e)
                print('取得できませんでした')
                pass

    path_w = './post_data.csv'
    with open(path_w, mode='w') as f:
        writer = csv.writer(f)
        for result_list in result_lists:
            writer.writerow(result_list)
