# モバイルスペースのスクレイピングスクリプト

## 概要
2020年9月末でサービス終了してしまう[モバイルスペース](http://m-space.jp/)の投稿データを何とかして投稿データを残したいと思い作成した、データをスクレイピングするスクリプトです。  

※SeleniumというPythonのライブラリで作成しています。  
事前にSChromeDriverをダウンロードする必要があります。  

※9/6 掲示板の投稿を取得するスクリプトしか組んでいません。
※即興で作成したので、ページ設定等が異なると動かないかもです。[Twitter](https://twitter.com/akisora001)などで相談ください。

## 準備
### Pythonのインストール

Pythonをインストールしてください  
こちらからインストールできます。
※Pythonのパスも通してください。
[Pythonの公式ページ](https://www.python.org/)

### ChromeDriverのダウンロード  
公式のサイトからダウンロードしてください。  
[ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads)

### chromedriverのパスを通す  
ダウンロードしたchromedriverのパスを通します。  
以下のダブルクォーテーション（""）で囲まれているところにパスを記載してください。  

例：Macでアプリケーション配下に配置したなら  
```
chromedriver = "/Applications/chromedriver"
```
例：Windowsで「C:\chromedriver」のフォルダに配置したなら
```
chromedriver = "C:\chromedriver\chromedriver.exe"
```

### git clone  
適当な場所に`git clone`してください

### 必要なライブラリのインストール
Pythonの必要なライブラリをインストールします。
```
$ pip install -r requirements.txt
```

### URL・ページ数の記載
取得したいモバスペ掲示板URLとページ数を記載します。
```
# スクレイピングするURLを記載する
url = 'http://12.xmbs.jp/LACOWEGOUNI-**************-rl.php?guid=on'
# どこまでのページを取得するか記載する
page_num = 500
```

## 使い方
以下を実行します。  
```
$ python mobile_space_scrayping.py
```

うまく成功すると`post_data.csv`が出力されます。