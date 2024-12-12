import requests
from bs4 import BeautifulSoup

# URL страницы
url = "https://www.py4e.com/"

# Получаем HTML-код страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все ссылки
links = soup.find_all('a', href=True)

# Фильтруем ссылки на внешние сайты (начинаются с http или https)
external_links = set()
for link in links:
    href = link['href']
    if href.startswith(('http://', 'https://')):
        external_links.add(href)

# Выводим количество уникальных ссылок
print(f"Количество уникальных внешних ссылок: {len(external_links)}")
