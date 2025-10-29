# web-scraping
爬蟲練習
scrape1 練習正規表達式和request請求

scrape2 示範如何使用 **Python 的 requests 與 BeautifulSoup (bs4)** 進行網頁資料擷取。
程式會自動連線到 [Books to Scrape](http://books.toscrape.com) 網站，
抓取指定分類（如旅遊 Travel 類）的所有書籍資訊，包含：
- 書名（title）
- 價格（price）
- 評分（rating）

最終會將結果以 JSON 格式輸出到檔案中。

scrape3

使用 Python 爬取博客來網站指定分類的書籍前 20 名資料，並將結果輸出為 JSON 與終端顯示。

## 功能

- 爬取指定網頁的書籍列表
- 解析書籍排名、書名、價格
- 篩選前 20 名書籍
- 格式化輸出於終端
- 儲存結果為 `books_info.json`（UTF-8 編碼）

## 技術

- Python 3
- requests
- BeautifulSoup4
- re（正則表達式）

## 使用方法

1. 安裝套件

```bash
pip install requests beautifulsoup4 lxml





