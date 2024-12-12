import requests
from bs4 import BeautifulSoup

# URL страницы
url = "https://py4e-data.dr-chuck.net/comments_42.html"

# Получаем HTML-код страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все комментарии (например, в тегах <span>)
comments = soup.find_all('span', class_='comments')

# Считаем общее количество комментариев
total_comments = sum(int(comment.text) for comment in comments)

# Выводим результат
print(f"Общее количество комментариев: {total_comments}")
