import requests, re


url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(url)

# Find all matches of the price pattern(找出所有符合價格模式的項目)
# 使用raw string避免跳脫字元的影響

match = re.findall(r'£\d+\.\d{2}', response.text)

# Print the matched prices(印出所有符合的價格)
print(match)
