import requests
import json
from bs4 import BeautifulSoup

# 使用 lxml 解析器 (推薦：速度快、容錯性強)
try:
    response = requests.get("http://books.toscrape.com/catalogue/category/books/travel_2/index.html")
    response.encoding = "utf-8"# 設定正確的編碼，歐元符號才能正確顯示
    response.raise_for_status()  # 確保請求成功
    soup = BeautifulSoup(response.text, "lxml")
    print("--- 使用 lxml 解析成功 ---")
    # print(soup.prettify()) # prettify() 可美化輸出，方便除錯
except requests.RequestException as e:
    print(f"網路請求失敗: {e}")
# 1. find_all(tag, attributes, recursive, string, limit, kwargs)

articles = soup.find_all('article', class_='product_pod')

#print("1. 尋找所有標籤為 article 且 class 為 'product_pod' 的元素: ", articles, sep='\n')
#titles = [article.h3.a.get('title') for article in articles]
books = []
for article in articles:
    title = article.h3.a.get('title')  #.h3.a 取得 h3 標籤下的 a 標籤，.get('title') 取得 title 屬性值
    price = article.find('p', class_='price_color').text  # 找到 p 標籤且 class 為 price_color，並取出文字內容
    rating = article.p.get('class')[1]  # 取得 class 中的第二個元素作為評分
#.get('title') 取得 title 屬性值，等同於 article.h3.a['title']，但前者在屬性不存在時不會拋出例外

    books.append(
        {"title": title, "price": price, "rating": rating}
    )
# 格式化輸出和存檔...

for book in books:
    print(
        f"書名: {book['title']:<40} | 評分: {book['rating']:<10} | 價格: {book['price']}"
    )

with open("books_info.json", "w", encoding="utf-8") as f:
    json.dump(books, f, ensure_ascii=False, indent=2)
print("\n資料已儲存至 books_info.json")

#print("1. 所有書籍標題: ", [book["title"] for book in books], sep='\n')



# products = soup.find('h3')
# print("2. 尋找所有標籤為 h3 的元素: ", [child.get('title') for child in products.children], sep='\n')



