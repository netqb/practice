import requests
from bs4 import BeautifulSoup

# URL страницы
url = "https://stackoverflow.com/jobs/companies"

# Получаем HTML-код страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все города (например, в тегах <span> или <div>)
cities = set()
for item in soup.find_all('div', class_='location'):
    city = item.text.strip()
    if city:
        cities.add(city)

# Выводим города в алфавитном порядке
sorted_cities = sorted(cities)
print("Города в вакансиях:")
for city in sorted_cities:
    print(city)
